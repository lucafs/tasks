from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gTask', views.get_tasks, name='get tasks'),
    path('pTask', views.post_task, name='post task'),
]
