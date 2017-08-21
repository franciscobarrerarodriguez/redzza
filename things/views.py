from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from profiles import views as viewsProfiles
from .models import Notice, CityNotice, Product, Color, Service, Image, Video, Commentary
from .serializers import NoticeSerializer, CityNoticeSerializer, ProductSerializer, ColorSerializer, ServiceSerializer, ImageSerializer, VideoSerializer, CommentarySerializer


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

    # Validacion del correo que se intenta registrar
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
            time = request.data.get('time', None)
            state = request.data.get('state', None)
            offer = request.data.get('offer', None)
            place = request.data.get('place', None)
            color = request.data.get('color', None)
            description = request.data.get('description', None)
            locations = request.data.get('locations', None)
            images = request.data.get('images', None)
            videos = request.data.get('videos', None)
            urgency = request.data.get('urgency', None)

            notice = Notice.create(profile, category, title, description, kind)
            Notice.updataOffer(notice, offer)
            Notice.updateLocation(notice, place)
            Notice.updateUrgency(notice, urgency)
            for file in images:
                Image.create(notice, file)
            for file in videos:
                Video.create(notice, file)
            for location in locations:
                CityNotice.create(location, notice)
            if thing == 'P':
                product = Product.create(notice, state)
                Color.create(color, product)
                return Response({'success': True, 'msg': 'product-posted'})
            elif thing == 'S':
                Service.create(notice, time)
                return Response({'success': True, 'msg': 'service-posted'})
            else:
                return Response({'success': True, 'msg': 'Thing not defined'})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
