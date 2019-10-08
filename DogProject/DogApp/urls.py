from django.urls import path
from . import views

urlpatterns = [
    path('', views.blankURL, name="blank"),
    path('dog/', views.index, name="index"),
    path('dog/edit/<int:dogID>/', views.editDog, name="editDog"),
    path('dog/delete/<int:dogID>/', views.deleteDog, name="deleteDog"),
]
