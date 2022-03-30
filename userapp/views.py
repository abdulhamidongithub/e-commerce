from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import Mijoz
from asosiy.models import Ichki, Mahsulot

class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')
    def post(self, request):
        if request.POST.get("parol") == request.POST.get("parol2"):
            u = User.objects.create_user(
                username=request.POST.get("email"),
                password=request.POST.get("parol")
            )
            Mijoz.objects.create(
                ism = request.POST["f"] + " " + request.POST["l"],
                email=request.POST.get("email"),
                jins = request.POST['jins'],
                user = u,
                tel = request.POST.get('tel'),
                mamlakat = request.POST.get('m'),
                shahar = request.POST.get('sh'),
            )
            from django.core.mail import send_mail
            from django.conf import settings
            subject = 'Alistyle'
            message = 'Alistylega xush kelibsiz.' \
                      'Maroqli xarid tilaymiz!'
            from django.template.loader import render_to_string
            xabar = render_to_string("email.html", context=True)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("email"),]
            send_mail(subject, xabar, email_from, recipient_list)
            return redirect("/user/login/")
        else:
            return redirect("/user/register/")

class LoginView(View):
    def get(self, request):
        return render(request, "page-user-login.html")
    def post(self, request):
        l = request.POST["login"]
        p = request.POST["parol"]
        a = authenticate(username = l, password = p)
        if a is not None:
            login(request, a)
            return redirect("home")
        else:
            return redirect("login")

class UserSettingsView(View):
    def get(self, request):
        mijoz = Mijoz.objects.get(user=request.user)
        return render(request, 'page-profile-setting.html',{'mijoz':mijoz})

    def post(self, request):
        if request.POST.get("forma") == "f1":
            mijoz = Mijoz.objects.get(user=request.user)
            mijoz.ism=request.POST['name']
            mijoz.email=request.POST['email']
            mijoz.mamlakat=request.POST['mamlakat']
            mijoz.shahar=request.POST['shahar']
            mijoz.zipcode=request.POST['zipcode']
            mijoz.tel=request.POST['tel']
            mijoz.save()
            return redirect('settings')
        elif request.POST.get("forma") == "f2":
            mijoz = Mijoz.objects.get(user=request.user)
            rasm = request.FILES.get("rasm")
            mijoz.rasm = rasm
            mijoz.save()
            return redirect('settings')

class MaxsulotQosh(View):
    def get(self, request):
        mijoz = Mijoz.objects.get(user=request.user)
        all = Mahsulot.objects.filter(mijoz=mijoz)
        return render (request, "page-profile-seller.html", {"mahsulotlar":all})

class MahsulotV(View):
    def get(self, request):
        ichki = Ichki.objects.all()
        return render(request, "sotish_uchun.html", {"ichkilar":ichki})

    def post(self, request):
        m = Mijoz.objects.get(user=request.user)
        pk = request.POST.get("ichki")
        ichki = Ichki.objects.get(id=pk)
        Mahsulot.objects.create(
            mijoz = m,
            narx=request.POST.get("narx"),
            brend=request.POST.get("brend"),
            batafsil=request.POST.get("batafsil"),
            yetkazish=request.POST.get("yetkazish"),
            kafolat=request.POST.get("kafolat"),
            rasm=request.FILES.get("rasm"),
            nom=request.POST.get("nom"),
            aksiya = request.POST.get("aksiya"),
            ichki = ichki,
            promoted = False
        )
        return redirect("/user/seller/")

class PromoteView(View):
    def get(self, request, pk):
        m = Mahsulot.objects.get(id=pk)
        m.promoted=True
        m.save()
        return redirect("/user/seller/")