from django.shortcuts import render, redirect
import speedtest
from geopy.geocoders import Nominatim
from gtts import gTTS
import os
# Create your views here.


def index(request):

    st = speedtest.Speedtest()
    x = st.download() * 9.537 * 0.0000001
    y = st.upload() * 9.537 * 0.0000001
    servernames = []

    z = st.get_servers(servernames)
    return render(request, 'index.html', {'d': x, 'u': y, 'ser': z})

def location(request):
        return render(request, 'location.html')


def go(request):
        loc = Nominatim(user_agent="GetLoc")
        getLoc = loc.geocode(request.GET['city'])

        return render(request, 'location.html', {"a": getLoc.address, "b": getLoc.latitude, "c": getLoc.longitude})

def home(request):
    return render(request, 'home.html')


def speech(request):
    return render(request, 'speech.html')

def conver(request):

        mytext = request.GET['text']
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("wel.mp3")
        os.system("wel.mp3")

        return render(request, 'speech.html')