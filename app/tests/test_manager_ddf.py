from django.test import TestCase
from app.models import AppSecond
from django_dynamic_fixture import G


class ManagerTest(TestCase):

    def setUp(self):
        G(AppSecond, name='Atest', n=3)
        G(AppSecond, name='Btest', n=2)

    def test_filter_a_name(self):
        result = AppSecond.objects.filter_a_name()
        self.assertTrue(result.exists())
        self.assertEqual(result.count(), 3)

    def test_filter_b_name(self):
        result = AppSecond.objects.filter_b_name()
        self.assertTrue(result.exists())
        self.assertEqual(result.count(), 2)

    def test_without_filter(self):
        result = AppSecond.objects.all()
        self.assertEqual(result.count(), 5)
