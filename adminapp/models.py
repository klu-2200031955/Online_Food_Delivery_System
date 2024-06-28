from django.db import models


# Create your models here

class Admin(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username
