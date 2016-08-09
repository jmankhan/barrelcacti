from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


# Stream music over http
def stream_music(request, song):
	print song
	resp = StreamingHttpResponse(stream_music_generator())
	return resp

def stream_music_generator():
	yield '<p>Test Stream</p>'
	for x in range(1, 11):
		yield '<div>Test %s</div>' % x
		yield ' ' * 1024
		time.sleep(1)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

