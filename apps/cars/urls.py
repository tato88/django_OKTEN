from django.urls import path

from .views import CarsListView, CarsRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarsListView.as_view()),
    path('/<int:pk>', CarsRetrieveUpdateDestroyView.as_view())
]
