from django.urls import path

from wechar import views

urlpatterns = [
    path('login/',views.login)
]