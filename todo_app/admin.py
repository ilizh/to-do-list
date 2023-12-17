from django.contrib import admin

from todo_app.models import Tag, Task


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("datetime_created", "is_done",)
    fieldsets = [
        ("Fields", {
            "fields": ["datetime_created", "is_done", "deadline_datetime", "content", "tags"],
        }),
    ]

