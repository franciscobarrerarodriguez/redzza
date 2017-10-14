from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from redzza import utils
from .models import Notice, CityNotice, Product, Color, Service, Image, Video, Commentary
from .serializers import NoticeSerializer, CityNoticeSerializer, ProductSerializer, ColorSerializer, ServiceSerializer, ImageSerializer, VideoSerializer, CommentarySerializer
from django.core import serializers
import json
from django.core.cache import cache


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    http_method_names = ['get', 'head', 'delete']

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.profile.user:
            return Response({'success': False, 'err': 'user-unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        instance.visibility = False
        instance.save()
        return Response({'success': True})

    # Obtencion de informacion de una notice
    @detail_route(methods=['get'])
    def getData(self, request, pk=None):
        try:
            notice = Notice.getNotice(pk)
            context = utils.noticeComplete(notice)
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Obtencion de comentarios de una notice
    @detail_route(methods=['get'])
    def getComments(self, request, pk=None):
        try:
            notice = Notice.getNotice(pk)
            context = []
            for i, commentary in enumerate(Commentary.search(notice)):
                profile = utils.getProfileSimple([commentary.profile])
                notice = utils.getDataNotice([commentary.notice], False)
                commentarySerialized = json.loads(serializers.serialize('json', [commentary]))
                context.append({'commentary': commentarySerialized, 'notice': notice, 'profile': profile})
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class CityNoticeViewSet(viewsets.ModelViewSet):
    queryset = CityNotice.objects.all()
    serializer_class = CityNoticeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ['post', 'head', 'delete']

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        notice = Notice.getNotice(request.data['notice'])
        if request.user != notice.profile.user:
            return Response({'success': False, 'err': 'user-unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.notice.profile.user:
            return Response({'success': False, 'err': 'user-unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        self.perform_destroy(instance)
        return Response({'success': True})


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    http_method_names = ['post', 'head', 'delete']

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        notice = Notice.getNotice(request.data['notice'])
        if request.user != notice.profile.user:
            return Response({'success': False, 'err': 'user-unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.notice.profile.user:
            return Response({'success': False, 'err': 'user-unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        self.perform_destroy(instance)
        return Response({'success': True})


class CommentaryViewSet(viewsets.ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer
    http_method_names = ['post', 'head', 'put', 'delete']

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        profile = utils.getProfile(request.user)
        request.data['profile'] = profile.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        profile = utils.getProfile(request.user)
        request.data['profile'] = profile.id
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if request.user != instance.profile.user:
            return Response({'success': False, 'err': 'user-unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.profile.user:
            return Response({'success': False, 'err': 'user-unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        self.perform_destroy(instance)
        return Response({'success': True})


class ApiServicesViewSet(viewsets.ViewSet):

    # Nueva publicacion de producto o servicio
    @list_route(methods=['post'])
    def newNotice(self, request):
        try:
            user = request.user
            profile = utils.getProfile(user)
            # KIND: 1 --> have; 2 --> search
            kind = request.data.get('kind', None)
            # THING P --> producto, S --> servicio
            thing = request.data.get('thing', None)
            title = request.data.get('title', None)
            category = request.data.get('category', None)
            place = request.data.get('place', None)
            description = request.data.get('description', None)
            locations = request.data.get('locations', None)
            urgency = request.data.get('urgency', None)
            # busco
            offer = request.data.get('offer', None)
            # producto
            state = request.data.get('state', None)
            quantity = request.data.get('quantity', None)
            colors = request.data.get('colors', None)
            # servicio
            time = request.data.get('time', None)

            if kind is None or thing is None or title is None or category is None or place is None or description is None:
                return Response({'success': False, 'err': 'Incomplete data'}, status=status.HTTP_400_BAD_REQUEST)

            if thing == 'P' and (state is None or state == 'null'):
                return Response({'success': False, 'err': 'state undin'}, status=status.HTTP_400_BAD_REQUEST)

            if thing == 'S' and (time is None or time == 'null'):
                return Response({'success': False, 'err': 'Incomplete data'}, status=status.HTTP_400_BAD_REQUEST)

            notice = Notice.create(profile, category, title, description, kind, urgency, place)
            if locations:
                for location in locations:
                    CityNotice.create(location, notice)
            else:
                CityNotice.create(place, notice)
            noticeSerialized = json.loads(serializers.serialize('json', [notice]))
            if offer and kind == 2:
                try:
                    Notice.updateOffer(notice, offer)
                except Exception:
                    # "Non-existent offer"
                    pass
            if thing == 'P':
                product = Product.create(notice, state)
                if quantity:
                    Product.updateQuantity(product, quantity)
                if colors:
                    for color in colors:
                        Color.create(color, product)
                return Response({'success': True, 'msg': 'product-posted', 'notice': noticeSerialized})
            elif thing == 'S':
                Service.create(notice, time)
                return Response({'success': True, 'msg': 'service-posted', 'notice': noticeSerialized})
            else:
                return Response({'success': False, 'err': 'Thing not defined'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Edicion publicacion de producto o servicio
    @list_route(methods=['put'])
    def updateNotice(self, request):
        try:
            idnotice = request.data.get('notice', None)
            notice = Notice.getNotice(idnotice)
            product = Product.searchProduct(notice)
            service = Service.searchService(notice)
            title = request.data.get('title', None)
            category = request.data.get('category', None)
            place = request.data.get('place', None)
            description = request.data.get('description', None)
            locations = request.data.get('locations', None)
            urgency = request.data.get('urgency', None)
            visibility = request.data.get('visibility', None)
            # busco
            offer = request.data.get('offer', None)
            # Producto
            colors = request.data.get('colors', None)
            state = request.data.get('state', None)
            quantity = request.data.get('quantity', None)
            # Servicio
            time = request.data.get('time', None)

            if request.user != notice.profile.user:
                return Response({'success': False, 'err': 'user-unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

            if title:
                Notice.updateTitle(notice, title)
                return Response({'success': True, 'msg': 'title-update'})
            elif category:
                Notice.updateCategory(notice, category)
                return Response({'success': True, 'msg': 'category-update'})
            elif place:
                Notice.updatePlace(notice, place)
                return Response({'success': True, 'msg': 'place-update'})
            elif description:
                Notice.updateDescription(notice, description)
                return Response({'success': True, 'msg': 'description-update'})
            elif visibility:
                Notice.updateVisibility(notice, visibility)
                return Response({'success': True, 'msg': 'visibility-update'})
            elif locations:
                CityNotice.deleteAll(notice)
                for location in locations:
                    CityNotice.create(location, notice)
                return Response({'success': True, 'msg': 'locations-update'})
            elif urgency:
                Notice.updateUrgency(notice, urgency)
                return Response({'success': True, 'msg': 'urgency-update'})
            elif offer:
                if notice.kind == 2:
                    Notice.updateOffer(notice, offer)
                    return Response({'success': True, 'msg': 'offer-update'})
                else:
                    return Response({'success': False, 'err': 'kind is not 2'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif colors:
                if product:
                    Color.deleteAll(product)
                    for color in colors:
                        Color.create(color, product)
                    return Response({'success': True, 'msg': 'color-update'})
                else:
                    return Response({'success': False, 'err': 'this notice not is a product'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif state:
                if product:
                    Product.updateState(product, state)
                    return Response({'success': True, 'msg': 'state-update'})
                else:
                    return Response({'success': False, 'err': 'this notice not is a product'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif quantity:
                if product:
                    Product.updateQuantity(product, quantity)
                    return Response({'success': True, 'msg': 'quantity-update'})
                else:
                    return Response({'success': False, 'err': 'this notice not is a product'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif time:
                if service:
                    Service.updateTime(service, time)
                    return Response({'success': True, 'msg': 'time-update'})
                else:
                    return Response({'success': False, 'err': 'this notice not is a service'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:
                return Response({'success': False, 'err': 'field-undefined'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Busqueda de publicacion
    @list_route(methods=['post'])
    def searchNotice(self, request):
        try:
            title = request.data.get('title', None)
            categories = request.data.get('categories', None)
            locations = request.data.get('locations', None)
            kind = request.data.get('kind', None)

            if kind is None or kind > 2:
                return Response({'success': False, 'err': 'kind-undefined'}, status=status.HTTP_400_BAD_REQUEST)

            queries = []
            if title and categories and locations:
                for category in categories:
                    for location in locations:
                        queries.append(Notice.searchTitleCategoryCity(title, category, location, kind))
            elif categories and locations:
                for category in categories:
                    for location in locations:
                        queries.append(Notice.searchCategoryCity(category, location, kind))
            elif title and categories:
                for category in categories:
                    queries.append(Notice.searchTitleCategory(title, category, kind))
            elif title and locations:
                for location in locations:
                    queries.append(Notice.searchTitleCity(title, location, kind))
            elif categories:
                for category in categories:
                    queries.append(Notice.searchCategory(category, kind))
            elif locations:
                for location in locations:
                    queries.append(Notice.searchCity(location, kind))
            elif title:
                queries.append(Notice.searchTitle(title, kind))
            else:
                return Response({'success': False, 'err': 'fields-undefined'}, status=status.HTTP_400_BAD_REQUEST)
            notices = utils.noticesQuery(queries)
            context = utils.getDataNotice(notices)
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Autocompletado del buscador
    @list_route(methods=['post'])
    def searchPredictive(self, request):
        try:
            start = request.data.get('start', None)

            if start:
                context = Notice.predictive(start)
            else:
                return Response({'success': False, 'err': 'fields-undefined'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Autocompletado del buscador
    @list_route(methods=['post'])
    def searchPredictiveCache(self, request):
        try:
            start = request.data.get('start', None)

            if start:
                context = cache.get('start_%s' % start)
                if context is None:
                    context = Notice.predictive(start)
                    cache.set('start_%s' % start, context)
            else:
                return Response({'success': False, 'err': 'fields-undefined'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
