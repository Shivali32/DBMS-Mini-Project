from django.urls import path
from gym import views

urlpatterns = [ 
    path("", views.home, name="home"),
    path('EnterMember/', views.EnterMember),
    path('EnterTrainer/', views.EnterTrainer),
    path('showTrainer/', views.showTrainer),
    path('showMember/', views.showMember),
]