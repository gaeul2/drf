from django.shortcuts import render, redirect
from django_todo.models import DjangoTodo as DjangoTodoModel
from django_todo.forms import TodoForm


# Create your views here.
def show_not_complete_todos(request):
    incomplete_todos = DjangoTodoModel.objects.filter(complete=0).all()
    return render(request, 'django_todo/todo_list.html', {"todos": incomplete_todos})


def todo_detail(request, pk):
    clicked_todo = DjangoTodoModel.objects.get(id=pk)
    return render(request, 'django_todo/todo_detail.html', {"todo": clicked_todo})


def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)  # 시리얼라이저에서 data=request.data와 같은원리군
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
        return render(request, 'django_todo/todo_post.html', {'form': form})


def todo_edit(request, pk):
    todo = DjangoTodoModel.objects.get(id=pk)
    if request.method == "POST":  # <form method="POST"> action이 없으면 url이 현재url이기 떄문에 저장요청이 이 url로 옴
        form = TodoForm(request.POST, instance=todo)  # form에 객체를 전달할 떄 instance를통해 todo로 전달해줌
        # 역시 시리얼라이즈와 비슷하군
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    if request.method == "GET":  # GET일때 todo인스턴스의 내용이 담긴 폼을 html에 띄워줌.
        form = TodoForm(instance=todo)
        return render(request, 'django_todo/todo_post.html', {'form': form})


def done_todo(request, pk):
    todo = DjangoTodoModel.objects.get(id=pk)
    todo.complete = 1
    todo.save()
    return redirect('todo_list')


def show_done_list(request):
    done_todos = DjangoTodoModel.objects.filter(complete=1)
    return render(request, 'django_todo/done_list.html', {'dones':done_todos})
