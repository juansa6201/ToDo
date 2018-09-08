from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import *
from .models import ToDo

# Create your views here.

def get_list(request):
    if request.method=='POST':
        form = FormToDo(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user =request.user
            post.save()
            return redirect('../')
    else:
        form = FormToDo()

    return render(request, 'list.html', {'form': form,
                                         'todo': ToDo.objects.all()})

def delete(request, ToDoList_id):
    obj = ToDo.objects.get(pk=ToDoList_id)
    obj.delete()
    return redirect('../')

def archive(request, ToDoList_id):
    obj = ToDo.objects.get(pk=ToDoList_id)
    obj.archived = True
    obj.save()
    return redirect('../')