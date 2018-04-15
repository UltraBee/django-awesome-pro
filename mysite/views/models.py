from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()