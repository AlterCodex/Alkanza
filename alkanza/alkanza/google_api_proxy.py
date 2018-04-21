import requests
import numpy
from . import key as KEY


class Google_Api:

    def __init__(self):
        self._search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        self._details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        self._nearBy_url = "https://maps.googleapis.com/maps/api/place/radarsearch/json"
        pass
    
    def search_place(self,query):
        search_params={"key":KEY.key,"query":query}
        search_request = requests.get(self._search_url, params=search_params)
        search_result = search_request.json()
        #"?
        place_id = search_result["results"][0]["place_id"]
        location={'lat':0,'lon':0}
        location['lat']=search_result["results"][0]["geometry"]['location']['lat']
        location['lon']=search_result["results"][0]["geometry"]['location']['lng']
        return place_id,location
    
    def find_nearBy(self,location,radius,search_text):
        #location=-33.8670522,151.1957362&radius=500&keyword=cruise&key="
        location=str(location['lat'])+','+str(location['lon'])
        search_params={"location":location,'radius':str(radius),'keyword':search_text,"key":KEY.key}
        search_request = requests.get(self._nearBy_url, params=search_params)
        search_result = search_request.json()["results"]
        places_id = list(x["place_id"] for x in search_result)
        places_locations= list({'lat':x["geometry"]['location']['lat'],'lon':x["geometry"]['location']['lng']} for x in search_result)
        print(places_locations)
        return places_id,places_locations


