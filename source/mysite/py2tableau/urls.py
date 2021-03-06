from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_user_db', views.update_user_db, name='update_user_db'),
    path('check_user_db', views.check_user_db, name='check_user_db'),
    path('dashboards1', views.dashboards1, name='dashboards1'),
    path('dashboards', views.dashboards, name='dashboards'),
    path('dashboards2', views.dashboards2, name='dashboards2'),
    path('dashboards3', views.dashboards3, name='dashboards3'),
    path('infer', views.infer, name='infer'),
]
