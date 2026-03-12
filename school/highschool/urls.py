from django.urls import path
from . import views

urlpatterns = [
    path('highschool/', views.index, name='highschool'),
]