from django.urls import path
from . import views


urlpatterns =[
    path('',views.task_list,name = 'task_list'),
    path('create/',views.task_create,name = 'task_create'),
    path('complete/<int:pk>/',views.task_complete,name = 'task_complete'),
    path('delete/<int:pk>/',views.task_delete,name ='task_delete'),    
    path('register/', views.register, name = "register"),
    path('login/',views.user_login,name = 'login'),
    path('logout/',views.user_logout,name = 'logout'),
    path('edit/<int:pk>/', views.task_edit,name ='task_edit')
]