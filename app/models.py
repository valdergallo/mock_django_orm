from django.db import models
from app.managers import AppSecondManager


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

    objects = AppSecondManager()

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
