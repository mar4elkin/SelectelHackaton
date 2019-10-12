from django.urls                import path, include, re_path

from .views                     import *

urlpatterns = [
    path("task/<int:pk>", task_ditail, name="task_ditail"),
    path("task/add", add_task, name='add_task')
] 
