from django.test import TestCase
from app.models import AppOne, AppThird
import mock


class MockingTest(TestCase):

    def setUp(self):
        self.appOneMock = mock.Mock(spec=AppOne)
        self.appOneMock.name = 'Admin'
        self.appOneMock.description = 'Test'

    def test_get_admin_user(self):
        result = AppOne.get_full_description(self.appOneMock)
        self.assertEqual(result, u'Admin / Test')


class MockingThridTest(TestCase):

    def setUp(self):
        self.appThridMock = mock.Mock(spec=AppThird)
        self.appThridMock.name = 'Test'
        self.appThridMock.app_one.name = '1'

    def test_get_extra(self):
        result = AppThird.get_extra(self.appThridMock)
        self.assertEqual(result, u'1-Test')

    def test_get_extra_second(self):
        self.appThridMock.app_one.name = '2'
        self.appThridMock.app_second.name = '2'

        result = AppThird.get_extra(self.appThridMock)
        self.assertEqual(result, u'22-Test')
