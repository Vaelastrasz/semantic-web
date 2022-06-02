from django.urls import path

from . import views

app_name = 'Social'

urlpatterns = [
    path('create-person/', views.PersonCreationView.as_view(), name='person-creation'),
    path('update-person/<int:id>/', views.PersonUpdateView.as_view(), name='person-update'),
    path('get-person/<int:id>/', views.PersonRetrieveView.as_view(), name='person-retrieve'),
    path('list-person/', views.PersonListView.as_view(), name='person-list'),
    path('delete-person/<int:id>/', views.PersonDeleteView.as_view(), name='person-delete'),

    path('create-photo/', views.PhotoCreationView.as_view(), name='photo-creation'),
    path('update-photo/<int:id>/', views.PhotoUpdateView.as_view(), name='photo-update'),
    path('get-photo/<int:id>/', views.PhotoRetrieveView.as_view(), name='photo-retrieve'),
    path('list-photo/', views.PhotoListView.as_view(), name='photo-list'),
    path('delete-photo/<int:id>/', views.PhotoDeleteView.as_view(), name='photo-delete'),

    path('create-event/', views.EventCreationView.as_view(), name='event-creation'),
    path('update-event/<int:id>/', views.EventUpdateView.as_view(), name='event-update'),
    path('get-event/<int:id>/', views.EventRetrieveView.as_view(), name='event-retrieve'),
    path('list-event/', views.EventListView.as_view(), name='event-list'),
    path('delete-event/<int:id>/', views.EventDeleteView.as_view(), name='event-delete'),

    path('create-loc/', views.LocationCreationView.as_view(), name='loc-creation'),
    path('update-loc/<int:id>/', views.LocationUpdateView.as_view(), name='loc-update'),
    path('get-loc/<int:id>/', views.LocationRetrieveView.as_view(), name='loc-retrieve'),
    path('list-loc/', views.LocationListView.as_view(), name='loc-list'),
    path('delete-loc/<int:id>/', views.LocationDeleteView.as_view(), name='loc-delete'),

    path('create-holiday/', views.HolidayCreationView.as_view(), name='holiday-creation'),
    path('update-holiday/<int:id>/', views.HolidayUpdateView.as_view(), name='holiday-update'),
    path('get-holiday/<int:id>/', views.HolidayRetrieveView.as_view(), name='holiday-retrieve'),
    path('list-holiday/', views.HolidayListView.as_view(), name='holiday-list'),
    path('delete-holiday/<int:id>/', views.HolidayDeleteView.as_view(), name='holiday-delete'),

    path('create-promo/', views.PromotionCreationView.as_view(), name='promo-creation'),
    path('update-promo/<int:id>/', views.PromotionUpdateView.as_view(), name='promo-update'),
    path('get-promo/<int:id>/', views.PromotionRetrieveView.as_view(), name='promo-retrieve'),
    path('list-promo/', views.PromotionListView.as_view(), name='promo-list'),
    path('delete-promo/<int:id>/', views.PromotionDeleteView.as_view(), name='promo-delete'),

    path('create-price/', views.PriceCreationView.as_view(), name='price-creation'),
    path('update-price/<int:id>/', views.PriceUpdateView.as_view(), name='price-update'),
    path('get-price/<int:id>/', views.PriceRetrieveView.as_view(), name='price-retrieve'),
    path('list-price/', views.PriceListView.as_view(), name='price-list'),
    path('delete-price/<int:id>/', views.PriceDeleteView.as_view(), name='price-delete')
]