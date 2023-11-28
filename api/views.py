from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer

class ItemList(ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(item_location = location)
        
        return queryset

class ItemDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class LocationList(ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
