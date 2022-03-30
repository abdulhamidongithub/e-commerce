from django.urls import path
from .views import *

urlpatterns = [
    path('savat/', SavatView.as_view(), name = 'savat'),
    path('savat/<str:nom>/', SavatQoshView.as_view(), name = 'savat-qosh'),
    path('savat/<int:pk>/delete/',DeleteSavat.as_view(),name='delete'),
    path('tanlangan/',TanlanganView.as_view(),name='tanlangan'),
    path('like/<int:pk>/',LikeView.as_view(),name='likebosilgan'),
    path('tanlangan/delete/<int:son>/',DeleteTan.as_view(),name='tanlangandel'),
    path('',BuyurtmaView.as_view(),name='buyurtma'),
    path('qosh/',BuyurtmaqoshishView.as_view(),name='buyurtmaqoshish'),
]
