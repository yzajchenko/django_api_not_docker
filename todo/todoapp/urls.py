from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskViewDetail.as_view(), name='task-detail'),
    path('category/', CategoryView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryViewDetail.as_view(), name='category-detail'),
    path('priority/', PriorityView.as_view(), name='priority-list'),
    path('priority/<int:pk>/', PriorityViewDetail.as_view(), name='priority-detail'),



]

