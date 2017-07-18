from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notice, CityNotice, CategoryTrade, Product, Color, Service, Image, Video
from profiles.models import Profile
from categories.models import Category
from django.shortcuts import get_object_or_404
# Create your views here.


# Vista para el formulario de una nueva publicacion de una cosa
@login_required
def post(request):
    return render(request, 'post.html')

# Vista ajax que recibe nueva publicacion de cosa
@login_required
def newPost(request):
    # user = request.user
    # profile = get_object_or_404(Profile, user=user)
    # thing = request.POST.get('thing', None)
    # title = request.POST.get('title', None)
    # description = request.POST.get('description', None)
    # category_father = get_object_or_404(Profile, pattern=request.POST.get('category_father', None))
    # category_son = request.POST.get('category_son', None)
    # locations = request.POST.get('locations', None)
    # place = request.POST.get('place', None)
    # i_search = request.POST.get('i_search', None)
    # i_have = request.POST.get('i_have', None)

    # if thing == 'P':
    #     # donde agrego las dos categorias ??????????????????
    #     notice = Notice.create(profile, category, title, description, optionTrade)
    #     cityNotice = CityNotice.create(city, notice)
    #     categoryTrade = CategoryTrade.create(category, notice)
    #     product = Product.create(notice, quantity)
    #     color = Color.create(hexa, product)
    #     service = Service.create(notice, time)
    #     image = Image.create(notice, image)
    #     video = Video.create(notice, video)
    #     return JsonResponse({'success': True, 'url': '/dashboard/'})
    # else:
    return JsonResponse({'success': True, 'url': '/dashboard/'})
