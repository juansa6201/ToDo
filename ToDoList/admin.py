from django.contrib import admin
from .models import (ToDo)

# Register your models here.

class ToDoArchived(admin.ModelAdmin):
    list_filter = ('archived',)


admin.site.register(ToDo, ToDoArchived)



