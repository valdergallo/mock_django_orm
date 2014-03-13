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
        self.app = AppOne.objects.create(name='Admin', description='Test')

    def test_get_admin_user(self):
        result = self.app.get_full_description()
        self.assertEqual(result, u'Admin / Test')
