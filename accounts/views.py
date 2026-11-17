from django.shortcuts import render, redirect
from .forms import RegisterForm
from jobs.models import Job, Application
from .models import Profile
from django.contrib.auth.decorators import login_required

# Home page
def home(request):

    total_jobs = Job.objects.count()
    total_applications = Application.objects.count()

    context = {
        "total_jobs": total_jobs,
        "total_applications": total_applications,
    }

    return render(request, "jobs/home.html", context)

# Register page
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.save()

            user.profile.role = form.cleaned_data["role"]
            user.profile.save()
            return redirect("/accounts/login/")
        else:
            print(form.errors)
    else:  
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

@login_required
def dashboard(request):
    if request.user.profile.role == "recruiter":
    
        return redirect("recruiter_dashboard")
    else:
        return redirect("job_list")

