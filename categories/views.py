from django.core import serializers
from django.http import JsonResponse
from categories.models import Category
# Create your views here.


# Vista de obtencion de categorias
def getCategories(request):
    data = Category.objects.order_by('name')
    data_serialized = serializers.serialize('json', data)
    return JsonResponse(data_serialized, safe=False)
