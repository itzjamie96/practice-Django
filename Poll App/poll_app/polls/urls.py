from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('createpoll/', views.createPoll, name='createPoll'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/updatepoll/', views.updatePoll, name='updatePoll'),
    path('<int:pk>/deletepoll/', views.deletePoll, name='deletePoll'),
    path('<int:pk>/vote/', views.vote, name='vote'),
    path('randompoll/', views.randomPoll, name='randomPoll'),

]
