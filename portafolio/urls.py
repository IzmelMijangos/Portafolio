from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.send_contact_email, name='contacto'),
    path('health/', views.health_check, name='health_check'),
]