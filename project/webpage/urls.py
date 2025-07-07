from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('about/', views.about, name='about'),
    path('indix/', views.indix, name='indix'),
    path('contact/', views.contact, name='contact'),
]