from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'landing'
urlpatterns = [
    path('', views.login, name='login'),
    #path('selectcourses/', views.selectcourses, name='selectcourses'),
    path('selectcourses/<int:pk>', views.selectcourses, name='selectcourses'),
    #path('selectcourses/(?P<pk>\d+)/$', RedirectView.as_view(url='/landing/selectcourses/%(pk)/')),
    path('schedule/', views.schedule, name='schedule'),
    path('createuser/', views.createuser, name='createuser'),
]
