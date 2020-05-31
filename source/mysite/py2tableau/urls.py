from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_user_db', views.update_user_db, name='update_user_db'),
    path('check_user_db', views.check_user_db, name='check_user_db'),
    path('datasets', views.datasets, name='datasets'),
    path('dashboards', views.dashboards, name='dashboards'),
]
