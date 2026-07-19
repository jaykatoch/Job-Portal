from .resume_parser import extract_text_from_pdf
from .ai_matcher import calculate_match
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from .models import Job, Application
from .forms import ApplicationForm
from django.core.mail import send_mail 
from django.conf import settings

@login_required
def post_job(request):
    if request.user.profile.role != "recruiter":
        return redirect("dashboard")

        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            return redirect("recruiter_dashboard")
        else:
            print(form.errors)

    else:
        form = JobForm()

    return render(request, "jobs/post_job.html", {"form": form})


def job_list(request):
    jobs = Job.objects.all()
    return render(request, "jobs/job_list.html", {"jobs": jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, "jobs/job_detail.html", {"job": job})

@login_required
def apply_job(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user

            # Save application
            application.save()

            # Read resume
            resume_text = extract_text_from_pdf(application.resume.path)

            # Calculate AI match score
            score = calculate_match(resume_text, job.skills)

            # Save score
            application.match_score = score
            application.save()

            # Send confirmation email
            send_mail(
                subject="Application Submitted Successfully",
                message=f"""
Dear {request.user.username},

You have successfully applied for the position of {job.title} at {job.company}.

Your AI Match Score: {score:.2f}%

Thank you for using AI Resume Screening System.

Regards,
AI Resume Screening System
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=False,
            )

            return redirect("/jobs/")

    else:
        form = ApplicationForm()

    return render(request, "jobs/apply_job.html", {
        "form": form,
        "job": job
    })


from django.shortcuts import redirect

@login_required
def recruiter_dashboard(request):
    if request.user.profile.role != "recruiter":
        return redirect("dashboard")   # or redirect("job_list")

    applications = Application.objects.filter(
        job__recruiter=request.user
    ).select_related("job", "applicant").order_by("-match_score")

    selected = applications.filter(match_score__gte=70).count()
    shortlisted = applications.filter(match_score__gte=50, match_score__lt=70).count()
    rejected = applications.filter(match_score__lt=50).count()

    return render(request, "jobs/recruiter_dashboard.html", {
        "applications": applications,
        "selected": selected,
        "shortlisted": shortlisted,
        "rejected": rejected,
    })

    return render(
        request,
        "jobs/recruiter_dashboard.html",
        context
    )

@login_required
def resume_score(request):
    application = Application.objects.filter(
        applicant=request.user
    ).order_by("-id").first()

    return render(
        request,
        "jobs/resume_score.html",
        {"application": application}
    )

@login_required
def my_applications(request):
    applications = Application.objects.filter(applicant=request.user)

    return render(
        request,
        "jobs/my_applications.html",
        {"applications": applications},
    )

@login_required
def home(request):
    return render(request, "jobs/home.html")