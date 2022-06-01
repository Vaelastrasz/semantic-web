from django.urls import path

from . import views

app_name = 'Social'

urlpatterns = [
    path('create-person/', views.PersonCreationView.as_view(), name='person-creation'),
    path('update-person/<int:id>/', views.PersonUpdateView.as_view(), name='person-update'),
    path('get-person/<int:id>/', views.PersonRetrieveView.as_view(), name='person-retrieve'),
    path('delete-person/<int:id>/', views.PersonDeleteView.as_view(), name='person-delete')
]