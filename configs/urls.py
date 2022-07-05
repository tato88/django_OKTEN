from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users', include('apps.users.urls')),
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.auto_parks.urls'))
]
