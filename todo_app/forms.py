from django import forms
from .models import Tag, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline_datetime', 'tags']
        widgets = {
            'deadline_datetime': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline_datetime', 'tags']


class TagUpdateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
