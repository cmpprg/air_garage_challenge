from django.urls import path
from yelp_service import views

urlpatterns = [
    path(
      'bad_parking/<location>',
      views.YelpServiceView.as_view(),
      name = 'bad_parking'
    )
]
