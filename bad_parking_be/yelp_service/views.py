from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import requests

class YelpServiceView(View):
  def get(self, request, location):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
      'Authorization': 'Bearer mi5qSSqdhmrNXBjLq5MBMwuqcS0q8aE4u52fwqrG8CkrBjjksgdV8ZblHdh4ThtDqQVFapfOwrCqadcTH4sJIMhQgEcWpc0bK_9ms_rJ1H-xMT1Amp4tmH_PhAg3X3Yx'
    }
    params = {
      'location': location,
      'sort_by': 'rating',
      'categories': 'parking, All'
    }

    initial_response = requests.get(url, headers=headers, params=params)
    initial_data = initial_response.json()

    offset = initial_data['total'] - 20
    params['offset'] = offset

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    return JsonResponse(data)
