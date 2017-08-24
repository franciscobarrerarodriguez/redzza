from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from profiles import views as viewsProfiles
from .models import Notice, CityNotice, Product, Color, Service, Image, Video, Commentary
from .serializers import NoticeSerializer, CityNoticeSerializer, ProductSerializer, ColorSerializer, ServiceSerializer, ImageSerializer, VideoSerializer, CommentarySerializer
from django.core import serializers
import json


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


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
