from django import forms
from .models import Job, Application

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        exclude = ['recruiter']
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control shadow-sm"
            })

        self.fields["description"].widget.attrs.update({
            "rows": 5,
            "placeholder": "Describe the job..."
        })

        self.fields["skills"].widget.attrs.update({
            "rows": 3,
            "placeholder": "Python, Django, SQL..."
        })

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["resume"]