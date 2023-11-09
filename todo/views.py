from django.shortcuts import render
<<<<<<< HEAD
from .models import Item
=======
>>>>>>> refs/remotes/origin/main

# Create your views here.


def get_todo_list(request):
<<<<<<< HEAD
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
=======
    return render(request, 'todo/todo_list.html')
>>>>>>> refs/remotes/origin/main
