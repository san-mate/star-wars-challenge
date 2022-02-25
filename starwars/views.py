
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings


class Skywalkers(APIView):

    def get(self, request, format=None):
        """
        Return a description containing the titles of starwars movies that all the skywalkers participated.
        """
        description = ""
        
        people_search_url = settings.STARWARS_BASE_API + 'people/?search=skywalker'
        response = requests.get(people_search_url)
        
        for person in response.json()['results']:
            character_description = f"{person['name']} participated in "
            
            for i, film_url in enumerate(person['films']):
                r = requests.get(film_url)
                title = r.json()['title']
                
                character_description += title
                if (i==len(person['films'])-1):
                    character_description += ". "
                elif (i==len(person['films'])-2):
                    character_description += " and "
                else:
                    character_description += ", "
                
            description += character_description
        
        return Response({"description": description.strip()})