from django.shortcuts import render
from django.http import HttpResponse
import json
import time
from .models import *
# Create your views here.
def index(request):
    albumset = Album.objects.all()
    trackset = Track.objects.all()
    memberset = Member.objects.all()
    storyset = Story.objects.all()[0]

    albums = [{'title': a.title, 'description': a.description, 'release_date': a.release_date,
    	'img': a.img, 'id': a.pk} for a in albumset]
    tracks = [{'title': t.title, 'length': t.length, 'album': t.album.pk} for t in trackset]
    members = [{'first_name': m.first_name, 'last_name': m.last_name, 'bio': m.bio, 'id':m.pk} for m in memberset]
    story = {'title': storyset.title, 'text': storyset.text}

    return render(request, 'index.html', {'albums' : albums, 'tracks' : tracks, 'members' : members, 'story': story})


def db(request):
	albums = Album.objects.all()
	return render(request, 'db.html', {'albums' : albums})