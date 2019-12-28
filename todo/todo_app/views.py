from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem
# Create your views here.
def todoViews(request):
    all_todo_item=TodoItem.objects.all()
    return render(request,'home.html',
    {'all_item':all_todo_item })

def addTodo(request):
    new_item=TodoItem(content= request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')

def deleteTodo(request,todo_id):
    item_delete= TodoItem.objects.get(id=todo_id)
    item_delete.delete()
    return HttpResponseRedirect('/')
