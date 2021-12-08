from django.urls import include, path
from django.contrib import admin
from django.urls import path

import views

urlpatterns = [
    path('', views.index, name='index'),
]


urlpatterns = [
    path('polls/', include('urls.py')),
    path('admin/', admin.site.urls),
]
