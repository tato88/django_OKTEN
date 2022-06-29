from rest_framework.generics import ListCreateAPIView, CreateAPIView, DestroyAPIView, ListAPIView

from .serializers import AutoParksSerializer
from .models import AutoParksModel
from apps.cars.serializers import CarSerializer


class AutoParksListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParksSerializer


class AutoparkAddCarView(CreateAPIView):
    queryset = AutoParksModel
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)


class AutoParkDestroyView(DestroyAPIView):
    queryset = AutoParksModel
    serializer_class = AutoParksSerializer
