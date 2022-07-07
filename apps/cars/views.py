from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .models import CarModel
from .serializers import CarSerializer
from permissions.user_permissions import IsSuperUser


class CarsListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsSuperUser,)

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
    permission_classes = (AllowAny,)
