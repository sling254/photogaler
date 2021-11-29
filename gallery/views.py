from django.http.response import HttpResponse
from django.shortcuts import render

from gallery.models import Image

# Create your views here.


def IndexView(request):
    title="HomePage"
    images = Image.objects.all()
    context ={
        "title":title,
        "images":images
    }
    return render (request,'index.html',context)

def searched_images(request):
    if request.method == "POST":
        searched = request.POST['searched']
        images = Image.search_photos_by_category(searched)       
        context={
            'searched':searched,
            "images":images,

        }

        return render(request,'searched_images.html',context)

    context ={
        "title":"searched Images",
    }


    return render(request,'searched_images.html',context)

def fillter_by_location_Nyeri(request):
    images = Image.filter_photo_by_location('Nyeri')
    

    context={"images":images,}
    return render(request,'fillter_by_location.html',context)

def fillter_by_location_Nairobi(request):
    images = Image.filter_photo_by_location('Nairobi')
    

    context={"images":images,}
    return render(request,'fillter_by_location.html',context)

def fillter_by_location_Naks(request):
    images = Image.filter_photo_by_location('Naks')
    

    context={"images":images,}
    return render(request,'fillter_by_location.html',context)