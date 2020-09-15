from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.list, name='list'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete')
]