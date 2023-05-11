from django.shortcuts import HttpResponse,redirect
from datetime import datetime

# Create your views here.


def hello_(request):
    if request.method == "GET":
        return HttpResponse("Hello! Its my project")

def redirect_to_youtube_view(request):
    if request.method == 'GET':
        return redirect("https://www.youtube.com")


def  now_date(request):
    if request.method == "GET":
        now_date = datetime.now()
        return HttpResponse(now_date)
def goodby(request):
    if request.method == "GET":
        return HttpResponse("Goodby user!")