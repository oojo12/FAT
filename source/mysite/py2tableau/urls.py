from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_user_db', views.update_user_db, name='update_user_db'),
    path('view_user_data', views.view_user_data, name='view_user_data'),
]
