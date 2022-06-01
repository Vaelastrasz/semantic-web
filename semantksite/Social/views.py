from rest_framework import generics, status
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


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


class PersonDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Person.objects.all()