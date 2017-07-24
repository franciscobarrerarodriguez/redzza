from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notice, CityNotice, CategoryTrade, Product, Color, Service, Image, Video
from profiles.models import Profile, Place
from categories.models import Category
import json
from django.shortcuts import get_object_or_404
# Create your views here.


# ---------------------------------VISTAS RENDER----------------------------------------

# URL --> POST
# Vista para el formulario de una nueva publicacion de una cosa
@login_required
def post(request):
    context = {}
    return render(request, 'post.html', context)


# ---------------------------------VISTAS AJAX----------------------------------------

# URL --> AJAX/NEWPOST
# Vista ajax que recibe nueva publicacion de cosa
@login_required
def newPost(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    # KIND: 1 --> have; 2 --> search
    kind = request.POST.get('kind', None)
    # THING P --> producto, S --> servicio
    thing = request.POST.get('thing', None)
    title = request.POST.get('title', None)
    category = request.POST.get('category', None)
    state = request.POST.get('state', None)
    offer = request.POST.get('offer', None)
    place = request.POST.get('place', None)
    description = request.POST.get('description', None)
    locations = request.POST.get('locations', None)
    images = request.POST.get('images', None)
    videos = request.POST.get('videos', None)
    urgency = request.POST.get('urgency', None)

    if thing == 'P':
        notice = Notice.create(profile, category, title, description, kind)
        Product.create(notice, state)
        for element in json.loads(locations):
            location = get_object_or_404(Place, id=element)
            CityNotice.create(location, notice)
        return JsonResponse({'success': True, 'msg': 'product-posted'})
    elif thing == 'S':
        notice = Notice.create(profile, category, title, description, kind)
        Service.create(notice)
        for element in json.loads(locations):
            location = get_object_or_404(Place, id=element)
            CityNotice.create(location, notice)
        return JsonResponse({'success': True, 'msg': 'service-posted'})
    else:
        return JsonResponse({'success': True, 'msg': 'Thing not defined'})
