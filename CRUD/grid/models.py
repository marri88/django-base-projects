from django.db import models


class Employer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        info = [self.name, self.email, self.contact]
        return info

    class Meta:
        db_table = 'employers'
