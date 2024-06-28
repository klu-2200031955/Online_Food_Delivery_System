from django.db import models


# Create your models here.
class Dealer(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=225, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phno = models.CharField(max_length=10, blank=False)
    username = models.CharField(max_length=225, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, default="sdp12")


    class Meta:
        db_table = "dealer_table"


    def __str__(self):
        return str(self.username)


class Item(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, blank=False)
    offer = models.IntegerField(blank=False)
    price = models.IntegerField(blank=False,null=True)
    # image = models.FileField(blank=False, upload_to="static/images", null=True)
    # promoted = models.BooleanField(default=False)
    cart = models.BooleanField(default=False)

    class Meta:
        db_table = "item_table"

    def __str__(self):
        return str(self.name)

