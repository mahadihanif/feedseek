from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('gallery.html', views.gallery, name="gallery"),
]