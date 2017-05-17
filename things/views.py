from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


# Vista para el formulario de una nueva publicacion de una cosa
@login_required
def post(request):
    return render(request, 'post.html')


# Vista ajax que recibe nueva publicacion de cosa
@login_required
def newPost(request):
    return render(request, 'post.html')


# # Vista para la creacion de un usuario
# def createUser(request):
#     thing = request.POST.get('thing', None)
#     title = request.POST.get('title', None)
#     description = request.POST.get('description', None)
#     category_father = request.POST.get('category_father', None)
#     category_son = request.POST.get('category_son', None)
#     locations = request.POST.get('locations', None)
    
#     place = request.POST.get('place', None)
#     i_search = request.POST.get('i_search', None)
#     i_have = request.POST.get('i_have', None)

#     if email and username and name and last_name and password and place and i_search and i_have:
#         user, created = Profile.createUser(email, username, name, last_name, password)
#         if created:
#             # #######################################################
#             profile = Profile.create(place, user)
#             # i_have(Ofrezco) --> 1 ; i_search(Busco) --> 2
#             for element in json.loads(i_have):
#                 WantedCategory.create(element['pk'], profile, 1)
#             for element in json.loads(i_search):
#                 WantedCategory.create(element['pk'], profile, 2)
#             # #######################################################
#             login(request, user)
#             return JsonResponse({'success': True, 'url': '/dashboard/'})
#         else:
#             return JsonResponse({'success': False, 'err': 'User not created'})
#     else:
#         return JsonResponse({'success': False, 'err': 'Incomplete data'})
