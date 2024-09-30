from django.urls import path
from . import views


urlpatterns = [
    path('soup/', views.soup, name="soup recipe"),
]
