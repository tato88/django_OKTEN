from django.urls import path

from .views import AutoParksListCreateView, AutoparkAddCarView, AutoParkDestroyView

urlpatterns = [
    path('', AutoParksListCreateView.as_view()),
    path('/<int:pk>/cars', AutoparkAddCarView.as_view()),
    path('/<int:pk>', AutoParkDestroyView.as_view())
]
