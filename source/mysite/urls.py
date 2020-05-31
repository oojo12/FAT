from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('py2tableau/', include('py2tableau.urls')),
    path('admin/', admin.site.urls),
]
