from django.contrib import admin
from Social.models import Person, Event, Location, Photo, CustomUser

admin.site.register(Person)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Photo)
admin.site.register(CustomUser)