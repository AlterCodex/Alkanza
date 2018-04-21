from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.http import Http404
from . import key as KEY
from . import forms 
from . import google_api_proxy as google_maps
from . import distances_calculator as calculator

def home(request):
    if request.method== 'POST':
        try:
            form = forms.SearchForm(request.POST)
            if form.is_valid():
                google=google_maps.Google_Api()
                place=form.cleaned_data['search_address']
                radius=form.cleaned_data['radius']
                search_text=form.cleaned_data['key_word']
                (place_id,location)=google.search_place(place)
                (places,locations)=google.find_nearBy(location,radius,search_text)
                cal=calculator.Distance_Calculator()
                distances=cal.calculate_distances(location,locations)
                unbalanced_distance=cal.unbalanced_distance(distances)
                print(place_id)
                return render(request,'search_place.html',{'place_uid':str(place_id),'key':KEY.key,'unbalanced_distance':unbalanced_distance,'key_word':search_text})
        except Exception as ex:
            print(str(ex))
            request.method='GET'
            return render(request,'home.html',{'seachrForm':form,'errorMessage':'invalid Search Parameters'})
    return render(request,'home.html',{'seachrForm':forms.SearchForm(),'errorMessage':None})


def search_place(request):
    if request.method == 'POST':
        return render(request,'search_place.html',{'place_uid':place_id,'key':key})
    else:
        raise  Http404("Url not Found")
    