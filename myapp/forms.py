from django import forms

class ResumeForm(forms.Form):
    job_title = forms.ChoiceField(choices=[
        ("Data Analyst", "Data Analyst"),
        ("Software Engineer", "Software Engineer"),
        ("Project Manager", "Project Manager"),
        ("Machine Learning Engineer", "Machine Learning Engineer")
    ])
    resume_file = forms.FileField()
