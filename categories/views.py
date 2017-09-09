from rest_framework import viewsets, status
from .models import Category, WantedCategory, SuggestedCategory
from .serializers import CategorySerializer, WantedCategorySerializer, SuggestedCategorySerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.filter(pattern=None)
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    # Obtencion de subcategorias de un macro
    @detail_route(methods=['get'])
    def getSubCategories(self, request, pk=None):
        try:
            categories = Category.getSubCategories(pk)
            context = getDataCategories(categories)
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class WantedCategoryViewSet(viewsets.ModelViewSet):
    queryset = WantedCategory.objects.all()
    serializer_class = WantedCategorySerializer


class SuggestedCategoryViewSet(viewsets.ModelViewSet):
    queryset = SuggestedCategory.objects.all()
    serializer_class = SuggestedCategorySerializer


# obtener data de una lista de cidaddes
def getDataCategories(categories):
    context = []
    for category in categories:
        if category.pattern is None:
            context.append({'id': category.id, 'pattern': None, 'name': category.name})
        else:
            context.append({'id': category.id, 'pattern': category.pattern.id, 'name': category.name})
    return context
