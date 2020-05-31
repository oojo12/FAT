from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_user_db', views.update_user_db, name='update_user_db'),
    path('tableau', views.tableau, name='tableau'),
    path('check_user_db', views.check_user_db, name='check_user_db')
]
