from django.urls import path
from .views import *

urlpatterns = [
    path('', Home2.as_view(), name="home2"),
    path('home/', Home.as_view(), name="home"),
    path('bolim/', BolimView.as_view(), name="bolim"),
    path('bolim/<str:nom>/', IchkiView.as_view(), name="ichki"),
    path('ichki/<str:nom>/', MahsulotlarView.as_view(), name="mahsulotlar"),
    path('mahsulot/<str:nomi>/', MahsulotView.as_view(), name="mahsulot"),
]

