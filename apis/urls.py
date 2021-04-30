from django.urls import path
from .views import ListTodo, DetailTodo,ListTodoRetrieveDestroy

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('<int:pk>',  ListTodoRetrieveDestroy.as_view()),
]