from django.http.response import Http404
from django.shortcuts import render
from django.http  import HttpResponse

from gallery.models import Image

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    # imports photos and save it in database
    photo = Image.objects.all()
    return render(request, 'all-photos/index.html',{'photo':photo})

