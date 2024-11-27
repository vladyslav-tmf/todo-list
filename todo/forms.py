from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tag"]
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "tag": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
        }
