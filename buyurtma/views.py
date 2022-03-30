from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import *

class SavatView(View):
    def get(self, request):
        m = Mijoz.objects.get(user = request.user)
        things = Savat.objects.filter(mijoz = m)
        narxlar = []
        aksiyalar = []
        for i in things:
            narxlar.append(i.mahsulot.narx)
            aksiyalar.append(i.mahsulot.narx * i.mahsulot.aksiya/100)
        return render(request, 'page-shopping-cart.html', {'things' : things,"aksiya":sum(aksiyalar),"narx":sum(narxlar), "umumiy":sum(narxlar) - sum(aksiyalar)})

class SavatQoshView(View):
    def get(self, request, nom):
        m = Mahsulot.objects.get(nom=nom)
        mijoz = Mijoz.objects.get(user=request.user)
        s = request.GET.get("son")
        Savat.objects.create(
            mahsulot=m,
            mijoz=mijoz,
        )
        return redirect("mahsulot", m.nom)

class DeleteSavat(View):
    def get(self, request, pk):
        savat = Savat.objects.get(id=pk)
        savat.delete()
        return redirect('savat')

class TanlanganView(View):
    def get(self, request):
        m = Mijoz.objects.get(user=request.user)
        t = Tanlangan.objects.filter(mijoz=m)
        return render(request, "page-profile-wishlist.html", {"tanlangan":t})

class LikeView(View):
    def get(self, request, pk):
        t = Mijoz.objects.get(user=request.user)
        m = Mahsulot.objects.get(id=pk)
        Tanlangan.objects.create(
            mijoz=t,
            mahsulot=m
        )
        return redirect('savat')
class DeleteTan(View):
    def get(self, request, son):
        d = Tanlangan.objects.get(id=son)
        d.delete()
        return redirect('tanlangan')

class BuyurtmaView(View):
    def get(self, request):
        m=Mijoz.objects.get(user=request.user)
        man=Manzil.objects.get(mijoz=m)
        b=Buyurtma.objects.filter(mijoz=m)
        return render(request, 'page-profile-orders.html', {"buyurtma":b, "manzil":man})

class BuyurtmaqoshishView(View):
    def get(self, request):
        m = Mijoz.objects.get(user=request.user)
        s = Savat.objects.filter(mijoz=m)
        narxlar = []
        aksiyalar = []
        for i in s:
            narxlar.append(i.mahsulot.narx)
            aksiyalar.append(i.mahsulot.narx * i.mahsulot.aksiya / 100)
        buyurtma = Buyurtma.objects.create(
            mijoz = m,
            summa = sum(narxlar) + 15000 - sum(aksiyalar)
        )
        for i in s:
            buyurtma.savat.add(i)
            buyurtma.save()
        return redirect("/buyurtma/savat/")



