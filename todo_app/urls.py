from django.urls import path
from .views import (
    HomeView, UpdateTaskView, DeleteTaskView,
    TagListView, AddTagView, UpdateTagView, DeleteTagView, AddTaskView, toggle_task_status_view, undo_task_view
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_task/', AddTaskView.as_view(), name='add-task'),
    path('update_task/<int:pk>/', UpdateTaskView.as_view(), name='update-task'),
    path('delete_task/<int:pk>/', DeleteTaskView.as_view(), name='delete-task'),
    path('undo-task/<int:pk>/', undo_task_view, name='undo-task'),
    path('toggle_task_status/<int:task_id>/', toggle_task_status_view, name='toggle-task-status'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('add_tag/', AddTagView.as_view(), name='add-tag'),
    path('update_tag/<int:pk>/', UpdateTagView.as_view(), name='update-tag'),
    path('delete_tag/<int:pk>/', DeleteTagView.as_view(), name='delete-tag'),
]


app_name = "todo_list"
