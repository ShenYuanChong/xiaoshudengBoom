from django.urls import path

from pachongApp.wechar import views

urlpatterns = [
    path('login/',views.login),
    path('check_login/',views.check_login)
]