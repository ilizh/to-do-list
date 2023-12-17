from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, Tag
from .forms import TaskForm, TagForm, TaskUpdateForm


class HomeView(ListView):
    model = Task
    template_name = 'todo_app/home.html'
    context_object_name = 'tasks'
    ordering = ['is_done', '-datetime_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_form'] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
        return redirect('todo_list:home')


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo_app/add_task.html'
    success_url = reverse_lazy('todo_list:home')


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'todo_app/update_task.html'

    def get_success_url(self):
        return reverse_lazy('todo_list:home')


class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('todo_list:home')


def undo_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    # Perform the undo action (update task status to not done)
    task.is_done = False
    task.save()

    return redirect('todo_list:home')


def toggle_task_status_view(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect('todo_list:home')


class TagListView(ListView):
    model = Tag
    template_name = 'todo_app/tag_list.html'
    context_object_name = 'tags'


class AddTagView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo_app/add_tag.html'
    success_url = reverse_lazy('todo_list:tag-list')


class UpdateTagView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'todo_app/update_tag.html'
    success_url = reverse_lazy('todo_list:tag-list')


class DeleteTagView(DeleteView):
    model = Tag
    success_url = reverse_lazy('todo_list:tag-list')
