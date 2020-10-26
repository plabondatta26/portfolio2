from django.db import models

# Create your models here.


class GetInTouch(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=False)
    email_address = models.EmailField()
    subject = models.CharField(max_length=100, blank=False, unique=False)
    message = models.CharField(max_length=1000, blank=False, unique=False)

    def __str__(self):
        return self.name


