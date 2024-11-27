from django.contrib import admin

from todo.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "preview_task_content", "created_at", "deadline", "is_done", "get_tags"
    ]
    search_fields = ["content", "tag__name"]
    list_filter = ["is_done", "deadline", "tag__name"]
    list_editable = ["is_done"]

    def preview_task_content(self, task):
        content = task.content[:50]

        if len(task.content) > 50:
            content += "..."

        return content

    def get_tags(self, task):
        return ", ".join([tag.name for tag in task.tag.all()])

    preview_task_content.short_description = "Content"
    get_tags.short_description = "Tags"
