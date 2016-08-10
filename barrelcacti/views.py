from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import Album
from .models import Track

# Create your views here.
def index(request):
    albums = Album.objects.all()
    print albums
    return render(request, 'index.html', {'albums' : albums})


# Stream music over http
def stream_music(request, track):
	print track
	resp = StreamingHttpResponse(stream_music_generator())
	return resp

def stream_music_generator():
	yield '<p>Test Stream</p>'
	for x in range(1, 11):
		yield '<div>Test %s</div>' % x
		yield ' ' * 1024
		time.sleep(1)

def db(request):
	albums = Album.objects.all()
	return render(request, 'db.html', {'albums' : albums})