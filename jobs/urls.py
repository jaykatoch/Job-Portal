from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("post-job/", views.post_job, name="post_job"),
    path("<int:id>/", views.job_detail, name="job_detail"),
    path("apply/<int:id>/",views.apply_job, name="apply_job"),
    path("dashboard/", views.recruiter_dashboard,name="recruiter_dashboard",),
    path("resume-score/", views.resume_score,name="resume_score"),
    path("my-applications/",views.my_applications,name="my_applications"),
    path("home/", views.home, name="home"),
]