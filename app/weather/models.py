from django.db import models


class City(models.Model):
    """Define city field"""
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    # define Meta class:in admin shows the plural of cities
    class Meta:
        verbose_name_plural = 'cities'
