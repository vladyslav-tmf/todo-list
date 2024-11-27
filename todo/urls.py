from django.urls import path

from todo import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/",
        views.TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        views.TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/complete/",
        views.TaskCompleteView.as_view(),
        name="task-complete"
    ),
    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag-create"),
    path(
        "tags/<int:pk>/update/",
        views.TagUpdateView.as_view(),
        name="tag-update"
    )
]
