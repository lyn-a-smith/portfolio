from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me_view, name='about_me'),
    path('contact/', views.contact_view, name='contact'),
    path('experience/', views.experience_view, name='experience'),
    path('thank-you', views.thank_you_view, name='thank_you')
]