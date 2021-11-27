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

#search results functions
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def photo(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/photo.html", {"image":image})