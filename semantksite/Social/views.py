from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Person, Photo, Event, Location, Price, Holiday, Promotion
from .serializers import PersonSerializer, PhotoSerializer, EventSerializer, LocationSerializer, PriceSerializer, HolidaySerializer, PromotionSerializer


class PersonCreationView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonListView(generics.ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Person.objects.all()



class PhotoCreationView(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

class PhotoRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

class PhotoListView(generics.ListAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

class PhotoDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Photo.objects.all()



class EventCreationView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Event.objects.all()



class LocationCreationView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationListView(generics.ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Location.objects.all()



class PriceCreationView(generics.CreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class PriceUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = PriceSerializer
    queryset = Price.objects.all()

class PriceRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = PriceSerializer
    queryset = Price.objects.all()

class PriceListView(generics.ListAPIView):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()

class PriceDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Price.objects.all()



class PromotionCreationView(generics.CreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class PromotionUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()

class PromotionRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()

class PromotionListView(generics.ListAPIView):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()

class PromotionDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Promotion.objects.all()



class HolidayCreationView(generics.CreateAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer

class HolidayUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()

class HolidayRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()

class HolidayListView(generics.ListAPIView):
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()

class HolidayDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Holiday.objects.all()    