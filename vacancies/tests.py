from django.test import TestCase, Client
from users.models import User


class VacanciesRoutesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user('user', 'user@gmail.com', '123456Test')
        user.is_employer = False
        user.save()
        employer = User.objects.create_user('employer', 'employer@gmail.com', '123456Test')
        employer.is_employer = True
        employer.save()

    def test_user_can_add_vacancy(self):
        self.client.login(username='user', password='123456Test')
        response = self.client.get('/vacancies/add-vacancy/')
        self.assertEqual(response.status_code, 403)

    def test_employer_can_add_vacancy(self):
        self.client.login(username='employer', password='123456Test')
        response = self.client.get('/vacancies/add-vacancy/')
        self.assertEqual(response.status_code, 200)
