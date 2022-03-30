from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('settings/',UserSettingsView.as_view(), name='settings'),
    path('seller/',MaxsulotQosh.as_view(), name='goodadd'),
    path('mahsulot/',MahsulotV.as_view(), name='user-mahsulot'),
    path('promote/<int:pk>/',PromoteView.as_view(), name='promote'),
]
