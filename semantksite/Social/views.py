from rest_framework import generics, status
from rest_framework.response import Response

from .models import Person, Photo, Event, Location
from .serializers import PersonSerializer, PhotoSerializer, EventSerializer, LocationSerializer


class PersonCreationView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonUpdateView(generics.RetrieveUpdateAPIView):
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

class PhotoUpdateView(generics.RetrieveUpdateAPIView):
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

class EventUpdateView(generics.RetrieveUpdateAPIView):
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

class LocationUpdateView(generics.RetrieveUpdateAPIView):
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