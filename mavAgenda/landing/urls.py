from django.urls import path

from . import views

app_name = 'landing'
urlpatterns = [
    path('', views.login, name='login'),
    path('selectcourses/', views.selectcourses, name='selectcourses'),
    path('schedule/', views.schedule, name='schedule'),
    path('createuser/', views.createuser, name='createuser'),
]
