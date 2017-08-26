from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from profiles import views as viewsProfiles
from .models import Notice, CityNotice, Product, Color, Service, Image, Video, Commentary
from .serializers import NoticeSerializer, CityNoticeSerializer, ProductSerializer, ColorSerializer, ServiceSerializer, ImageSerializer, VideoSerializer, CommentarySerializer
from django.core import serializers
from redzza.settings import MEDIA_URL
from django.contrib.sites.models import Site
import json


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    # Obtencion de informacion de una notice
    @detail_route(methods=['get'])
    def getData(self, request, pk=None):
        try:
            notice = Notice.getNotice(pk)
            context = {}
            context['notice'] = json.loads(serializers.serialize('json', [notice]))
            context['notice'][0]['fields']['location_name'] = str(notice.location)
            context['notice'][0]['fields']['category_name'] = str(notice.category)
            locations = CityNotice.searchCities(notice)
            context['notice'][0]['locations'] = {}
            for i, location in enumerate(locations):
                context['notice'][0]['locations'][i] = {'location': str(location.city.id), 'location_name': str(location.city)}
            current_site = 'http://%s' % (Site.objects.get(id=1).domain)
            images = Image.search(notice)
            context['notice'][0]['images'] = {}
            for i, image in enumerate(images):
                context['notice'][0]['images'][i] = {'id': str(image.id), 'image': current_site + MEDIA_URL + str(image.image)}
            videos = Video.search(notice)
            context['notice'][0]['videos'] = {}
            for i, video in enumerate(videos):
                context['notice'][0]['videos'][i] = {'id': str(video.id), 'video': current_site + MEDIA_URL + str(video.video)}
            thing = Notice.sortoutNotices([notice], False)[0]
            context['notice'][0]['thing'] = json.loads(serializers.serialize('json', [thing]))
            if thing.__class__ == Product:
                colors = Color.searchProduct(thing)
                context['notice'][0]['thing'][0]['fields']['colors'] = {}
                for i, color in enumerate(colors):
                    context['notice'][0]['thing'][0]['fields']['colors'][i] = {'color': str(color.hexa)}
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


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CommentaryViewSet(viewsets.ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer


class ApiServicesViewSet(viewsets.ViewSet):

    # Nueva publicacion de producto o servicio
    @list_route(methods=['post'])
    def newNotice(self, request):
        try:
            user = request.user
            profile = viewsProfiles.getProfile(user)
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
            colors = request.data.get('colors', None)
            # servicio
            time = request.data.get('time', None)

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
                    print("Non-existent offer")
            if thing == 'P':
                product = Product.create(notice, state)
                if colors:
                    for color in colors:
                        Color.create(color, product)
                return Response({'success': True, 'msg': 'product-posted', 'notice': noticeSerialized})
            elif thing == 'S':
                Service.create(notice, time)
                return Response({'success': True, 'msg': 'service-posted', 'notice': noticeSerialized})
            else:
                return Response({'success': True, 'msg': 'Thing not defined'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
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
            # Servicio
            time = request.data.get('time', None)
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
            notices = []
            for query in queries:
                for element in query:
                    if element.__class__ is Notice:
                        notices.append(element)
                    else:
                        notices.append(element.notice)
            notices = list(set(notices))
            context = []
            current_site = 'http://%s' % (Site.objects.get(id=1).domain)
            for i, notice in enumerate(notices):
                image = Image.search(notice)
                if len(image) > 0:
                    context.append({'id': notice.id, 'title': notice.title, 'image': current_site + MEDIA_URL + str(image[0].image), 'kind': "%s" % ("i_have" if notice.kind == 1 else "i_search")})
                else:
                    context.append({'id': notice.id, 'title': notice.title, 'image': current_site + MEDIA_URL + 'no_image.jpg', 'kind': "%s" % ("i_have" if notice.kind == 1 else "i_search")})
            if len(context) > 0:
                return Response({'success': True, 'data': context})
            else:
                return Response({'success': True, 'data': ''}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
