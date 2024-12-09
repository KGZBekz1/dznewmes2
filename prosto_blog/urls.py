from django.urls import path

from main.urls import urlpatterns
from  . import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.emoji, name='emoji'),
    path('photo/', views.image_proger_view, name='image_proger_view'),
]