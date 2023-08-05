
from django.urls import path, include
from . import views
urlpatterns = [
    
   path("", views.INDEX, name="index"),
   path('delete/<int:pk>',views.delete_emp, name="delete"),
   path('edit/<int:pk>',views.edit_emp, name="edit"),
   path('deletemultiple',views.delete_multiple, name="delete_multiple")
   
]