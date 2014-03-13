mock_django_orm
===============

Using mock to test django orm


Model Example
=============

```python

class AppOne(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def get_full_description(self):
        return u'%s / %s' % (self.name, self.description)

    def __unicode__(self):
        return self.name


class AppSecond(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class AppThird(models.Model):
    name = models.CharField(max_length=50)
    app_one = models.ForeignKey(AppOne)
    app_second = models.ForeignKey(AppSecond)

    def get_extra(self):
        if self.app_one.name == '1':
            return u'%s-%s' % (self.app_one.name, self.name)
        elif self.app_second.name == '1':
            return u'%s-%s' % (self.app_second.name, self.name)
        elif self.app_one.name == '2' and self.app_second.name == '2':
            return u'%s%s-%s' % (self.app_one.name,
                                 self.app_second.name,
                                 self.name)

```

Test Example
=============

```python

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

```
