from django.db import models


class AppSecondManager(models.Manager):

    def filter_a_name(self):
        return self.filter(name__startswith='a')

    def filter_b_name(self):
        return self.filter(name__startswith='b')
