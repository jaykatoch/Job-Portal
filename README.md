# 🤖 AI Job Portal – AI Resume Screening System

## 📌 Project Overview

AI Job Portal is a web-based application developed using Python and Django.

The system connects job seekers and recruiters through a common platform.
It allows candidates to browse jobs, upload resumes and track applications.

Recruiters can post jobs and manage applications. The system also provides
resume parsing and resume scoring functionality.

## 🎯 Objectives

- Simplify the job application process.
- Help recruiters manage job applications.
- Automate resume information extraction.
- Provide resume screening and scoring functionality.
- Connect candidates with recruiters.

## 🚀 Features

### 👨‍💻 Candidate Module
- User registration and login.
- Candidate dashboard.
- Browse available jobs.
- Apply for jobs.
- Upload PDF resumes.
- View application status.
- View resume scores.

### 👨‍💼 Recruiter Module
- Recruiter registration and login.
- Recruiter dashboard.
- Post new jobs.
- Manage job applications.
- Review candidate resumes.

### 🤖 AI Resume Screening
- PDF resume parsing.
- Resume text extraction.
- Resume scoring.
- Resume and job matching functionality.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML | Webpage structure |
| CSS | Styling |
| Bootstrap | Responsive design |
| JavaScript | Frontend functionality |
| SQLite | Database |
| pdfplumber | PDF text extraction |

## 📂 Project Structure

```text
Job-Portal/
│
├── accounts/
│   ├── migrations/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── jobportal/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── jobs/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── resume_parser.py
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│
├── manage.py
├── .gitignore
└── README.md
