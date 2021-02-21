from django.test import TestCase
from django.urls import reverse

class YelpServiceTestCase(TestCase):
  def test_successful_response_of_yelp_api(self):
    location = 'San Francisco'
    url = reverse('bad_parking', args=[location])

    response = self.client.get(url)

    self.assertEqual(response.status_code, 200)

    data = response.json()
    from IPython import embed; embed()
