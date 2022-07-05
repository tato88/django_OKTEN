from django.urls import path

from .views import AutoParksListCreateView, AutoparkAddCarView, AutoParksRetrieveDestroyView

urlpatterns = [
    path('', AutoParksListCreateView.as_view()),
    path('/<int:pk>/cars', AutoparkAddCarView.as_view()),
    path('/<int:pk>', AutoParksRetrieveDestroyView.as_view())
]
