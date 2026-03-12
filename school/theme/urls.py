from django.urls import path
from . import views

urlpatterns = [
    path('theme/', views.index, name='theme'),
]