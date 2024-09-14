from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',Index),
    path('home/',HomePage),
    path('addtask/',AddTask),
    path('viewtask/',ViewTask),
    path('Tasks/delete/<int:id>/',Delete_Task, name='task_delete'),
    path('Tasks/update/<int:id>/',Task_update, name='task_update'),
    path('filter/',Filter_Priority, name='filter')

    
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)