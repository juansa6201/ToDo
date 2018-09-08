from django.urls import path
from .views import get_list,delete,archive

urlpatterns = [
    path('', get_list, name="index"),
    path('delete/<int:ToDoList_id>', delete, name="delete"),
    path('archive/<int:ToDoList_id>', archive, name="archive")
]