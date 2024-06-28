from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Customer(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phno = models.CharField(max_length=10, blank=False, unique=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, default='sdp12')

    class Meta:
        db_table = "customer_table"

    def __str__(self):
        return str(self.username)



class Address(models.Model):
    username = models.CharField(max_length=100, blank=False)
    fullname = models.CharField(max_length=100, blank=False, null=True)
    email = models.CharField(max_length=100, blank=False, null=True)
    address = models.CharField(max_length=1000, blank=False, null=True)
    city = models.CharField(max_length=100, blank=False, null=True)
    state = models.CharField(max_length=100, blank=False, null=True)
    phno = models.CharField(blank=False, null=True)
    pincode = models.IntegerField(blank=False, null=True, validators=[
            MaxValueValidator(100000),
            MinValueValidator(999999)
        ])

    class Meta:
        db_table = "address_table"

    def __str__(self):
        return str(self.username)


class Card(models.Model):
    username = models.CharField(max_length=100,blank=False)
    chname = models.CharField(max_length=100, blank=False)
    cnumber = models.CharField(blank=False)
    expdate = models.CharField(blank=False)
    cvv = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(limit_value=999),
            MinValueValidator(limit_value=0),]
    )

    class Meta:
        db_table = "card_table"

    def __str__(self):
        return str(self.username)


class Upi(models.Model):
    username = models.CharField(max_length=100, blank=False)
    upi = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "upi_table"

    def __str__(self):
        return str(self.username)