from django.test import TestCase
from app.models import AppOne


class SimpleExample(TestCase):

    def test_true1(self):
        self.assertTrue(1)

    def test_true2(self):
        self.assertTrue(1)

    def test_true3(self):
        self.assertTrue(1)

    def test_true4(self):
        self.assertTrue(1)


class GetDataFromDefaultDB(TestCase):

    def setUp(self):
        AppOne.objects.create(name='admin', description='Test')

    def test_get_admin_user(self):
        admin = AppOne.objects.get(name='admin')
        self.assertTrue(admin.description)
