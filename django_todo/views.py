from django.shortcuts import render, redirect
from django_todo.models import DjangoTodo as DjangoTodoModel
from django_todo.forms import TodoForm

# Create your views here.
def show_not_complete_todos(request):
    incomplete_todos = DjangoTodoModel.objects.filter(complete=0).all()
    return render(request, 'django_todo/todo_list.html', {"todos":incomplete_todos})

def todo_detail(request, pk):
    clicked_todo = DjangoTodoModel.objects.get(pk=pk)
    return render(request, 'django_todo/todo_detail',{"todo" : clicked_todo})

def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST) #시리얼라이저에서 data=request.data와 같은원리군
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
        return render(request,'django_todo/todo_post.html',{'form':form})
