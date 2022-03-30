from django.db import models
from userapp.models import Mijoz

class Bolim(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.FileField(upload_to='bolim')
    def __str__(self):
        return self.nom

class Ichki(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.FileField(upload_to='ichki')
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True,related_name="bolim_ichkilari")
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.FileField(upload_to='mahsulot')
    mijoz = models.ForeignKey(Mijoz, blank=True, on_delete=models.SET_NULL, null=True)
    tasdiq = models.CharField(max_length=30, default="Tasdiqlangan")
    narx = models.IntegerField()
    batafsil = models.TextField()
    aksiya = models.PositiveSmallIntegerField(default=0)
    brend = models.CharField(max_length=50)
    kafolat = models.CharField(max_length=20)
    yetkazish = models.CharField(max_length=20)
    mavjud = models.BooleanField(default=True)
    promoted = models.BooleanField(default=True)
    mamlakat = models.CharField(max_length=30, blank=True, default="O'zbekiston")
    ichki = models.ForeignKey(Ichki, on_delete=models.SET_NULL, null=True,related_name="ichki_mahsulotlar")
    def __str__(self):
        return self.nom

class Baho(models.Model):
    baho = models.PositiveSmallIntegerField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True, related_name="mahsulot_baholari")
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)

