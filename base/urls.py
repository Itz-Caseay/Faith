from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/messages/', views.view_messages, name='view_messages'),
    path('admin/messages/mark-read/<int:message_id>/', views.mark_as_read, name='mark_as_read'),
]