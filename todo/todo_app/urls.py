from django.urls import path
from . import views
urlpatterns = [
    path('', views.todoViews, name='todoViews'),
    path('addTodo/', views.addTodo, name='addTodo' ),
    path('deleteTodo/<int:todo_id>/',views.deleteTodo, name='deleteTodo'),
]
