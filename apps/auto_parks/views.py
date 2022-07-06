from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .serializers import AutoParksSerializer
from .models import AutoParksModel
from apps.cars.serializers import CarSerializer


class AutoParksListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParksSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AutoParksRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParksSerializer
    permission_classes = (AllowAny,)


class AutoparkAddCarView(CreateAPIView):
    queryset = AutoParksModel
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)
