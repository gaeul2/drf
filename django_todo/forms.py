from django import forms
from django_todo.models import DjangoTodo as DjangoTodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = DjangoTodoModel
        fields = ("title", "description", "important")
