from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
    # Статусы
    path('statuses/', views.StatusListView.as_view(), name='status_list'),
    path('statuses/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('statuses/<int:pk>/update/', views.StatusUpdateView.as_view(), name='status_update'),
    path('statuses/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),

    # Метки
    path('labels/', views.LabelListView.as_view(), name='label_list'),
    path('labels/create/', views.LabelCreateView.as_view(), name='label_create'),
    path('labels/<int:pk>/update/', views.LabelUpdateView.as_view(), name='label_update'),
    path('labels/<int:pk>/delete/', views.LabelDeleteView.as_view(), name='label_delete'),
    
    # Задачи
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('test-rollbar/', views.test_rollbar, name='test_rollbar'),
]
