from django.urls import path

from .views import UserListCreateView, AddAvatarView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/avatars', AddAvatarView.as_view())
]
