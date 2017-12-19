from django.forms import ModelForm
from vacancies.models import Vacancy


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'location',
            'type',
            'email_for_resume',
            'description',
            'company_name',
            'company_site',
            'company_logo',
        ]