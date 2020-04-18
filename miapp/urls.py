from django.urls import path

from miapp import views

app_name = 'miapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('guardar', views.guardar, name='guardar'),
]