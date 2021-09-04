from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=130, blank=True)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    age = models.IntegerField(blank=True)

# model inheritance
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "cont"