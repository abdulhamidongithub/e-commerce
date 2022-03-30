from django.contrib.auth.models import User
from django.db import models

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    email = models.EmailField()
    jins = models.CharField(max_length=10, choices=[("Ayol","Ayol"), ("Erkak","Erkak")])
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    tel = models.CharField(max_length=15, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    mamlakat = models.CharField(max_length=30)
    shahar = models.CharField(max_length=30)
    rasm = models.FileField(upload_to="mijoz", blank=True, null=True)
    sana = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.ism

class Manzil(models.Model):
    mamlakat = models.CharField(max_length=30)
    shahar = models.CharField(max_length=30)
    manzil = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=7)
    default = models.BooleanField(blank=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    def __str__(self):
        return self.manzil

