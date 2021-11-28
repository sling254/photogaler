from django.http.response import HttpResponse
from django.shortcuts import render

from gallery.models import Image

# Create your views here.


def IndexView(request):
    title="HomePage"

    context ={
        "title":title,

    }
    return render (request,'index.html',context)

def searched_images(request):
    if request.method == "POST":
        searched = request.POST['searched']
        images = Image.search_photos_by_category(searched)
        print("This is what it has")
        print(images)
        context={
            'searched':searched,
            "images":images,

        }

        return render(request,'searched_images.html',context)

    context ={
        "title":"searched Images",
    }


    return render(request,'searched_images.html',context)