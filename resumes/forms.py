from django.forms import ModelForm
from resumes.models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = [
            'fio',
            'email',
            'title',
            'location',
            'photo',
            'industry',
            'summary',
            'resume_file',
            'skills',
            'experience',
        ]