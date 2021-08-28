from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=60)
    birthdate = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
