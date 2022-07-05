from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer


class CarsListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        # print(self.request.user.id)
        qs = self.queryset.all()
        auto_park_id = self.request.query_params.get('autoParkId')
        if auto_park_id:
            qs = qs.filter(auto_park_id=auto_park_id)
        return qs


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
