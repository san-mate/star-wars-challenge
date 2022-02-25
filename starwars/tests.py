from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class StarWarsTestCase(APITestCase):

    maxDiff = None

    def test_skywalker_description(self):
        expected_description = ("Luke Skywalker participated in A New Hope, The "
            "Empire Strikes Back, Return of the Jedi and Revenge of the Sith. "
            "Anakin Skywalker participated in The Phantom Menace, Attack of the "
            "Clones and Revenge of the Sith. Shmi Skywalker participated in The "
            "Phantom Menace and Attack of the Clones.")

        url = reverse('skywalker')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.data['description'], expected_description)