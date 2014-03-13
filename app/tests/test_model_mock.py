from django.test import TestCase
from app.models import AppOne, AppThird
import mock


class MockingTest(TestCase):

    def setUp(self):
        self.appOne = mock.Mock(spec=AppOne)
        self.appOne.name = 'Admin'
        self.appOne.description = 'Test'

    def test_get_admin_user(self):
        result = AppOne.get_full_description(self.appOne)
        self.assertEqual(result, u'Admin / Test')


class MockingThridTest(TestCase):

    def setUp(self):
        self.appThrid = mock.Mock(spec=AppThird)
        self.appThrid.name = 'Test'
        self.appThrid.app_one.name = '1'

    def test_get_extra(self):
        result = AppThird.get_extra(self.appThrid)
        self.assertEqual(result, u'1-Test')

    def test_get_extra_second(self):
        self.appThrid.app_one.name = '2'
        self.appThrid.app_second.name = '2'

        result = AppThird.get_extra(self.appThrid)
        self.assertEqual(result, u'22-Test')
