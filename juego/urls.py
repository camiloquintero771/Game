from django.urls import path
from . import views

urlpatterns = [
    path('juego/<int:num>', views.calcula, name="home"),
]