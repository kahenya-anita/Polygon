from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery

def home(request):
    return render(request, 'home.html')

def polygon(request):
    images = Gallery.objects.all()
    return render(request, 'photo.html', {'images':images})

def show(request, id):
    image = Gallery.objects.get(id=id)    
    return render(request, 'show.html', {'image':image})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search = request.GET.get("category")
        try:
            category = Category.objects.get(name = search)
            images = Image.search_image(category)
            message = f"Found {len(images)} image(s) under the category - {search}"
            return render(request, 'search.html',{"message":message,"images": images})
        except ObjectDoesNotExist:
            message = "NO ITEMS UNDER CATEGORY " + search.upper()
            categories = Category.objects.all()
            return render(request, 'search.html',{"message":message, "categories": categories}) 

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})
