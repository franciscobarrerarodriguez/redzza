from rest_framework import viewsets, status
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.decorators import list_route
from rest_framework.response import Response
from profiles import views as viewsProfiles
from things.models import Notice


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True})


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ApiServicesViewSet(viewsets.ViewSet):

    # Inicio de conversacion
    @list_route(methods=['post'])
    def startConversation(self, request):
        try:
            user = request.user
            profileSender = viewsProfiles.getProfile(user)
            idNotice = request.data.get('notice', None)
            notice = Notice.getNotice(idNotice)
            profileReceiver = notice.profile
            profiles = []
            profiles.append(profileReceiver)
            text = request.data.get('text', None)
            image = request.data.get('image', None)
            if (text or image) and notice and len(profiles) > 0:
                conversation = Conversation.create(profiles, notice)[0][0]
                Message.create(text, image, profileSender, conversation)
                return Response({'success': True, 'msg': 'conversation-created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'success': False, 'err': 'Incomplete data'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Agrega mensaje a una conversacion
    @list_route(methods=['post'])
    def addMessage(self, request):
        try:
            user = request.user
            profileSender = viewsProfiles.getProfile(user)
            idConversation = request.data.get('conversation', None)
            conversation = Conversation.getConversation(idConversation)
            text = request.data.get('text', None)
            image = request.data.get('image', None)

            if (text or image) and conversation and profileSender:
                Message.create(text, image, profileSender, conversation)
                return Response({'success': True, 'msg': 'message-created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'success': False, 'err': 'Incomplete data'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Obtiene inbox de un usuario
    @list_route(methods=['get'])
    def getInbox(self, request):
        try:
            user = request.user
            profile = viewsProfiles.getProfile(user)
            context = []
            conversations = []
            messagesSend = Message.searchConversationsSend(profile)
            for i, message in enumerate(messagesSend):
                conversations.append(messagesSend[i].conversation)
            conversationsReceived = Conversation.search(profile)
            for conversation in conversationsReceived:
                conversations.append(conversation)
            conversations = list(set(conversations))
            for conversation in conversations:
                listContestants = viewsProfiles.getProfileSimple(conversation.contestant.all())
                listReviews = viewsProfiles.getProfileSimple(conversation.review.all())
                listNotices = viewsProfiles.getDataNotice(conversation.notice.all(), fullData=False)
                listMessages = viewsProfiles.getDataMessages(Message.search(conversation))
                context.append({'id': conversation.id, 'modified': conversation.modified, 'contestants': listContestants, 'notices': listNotices, 'reviews': listReviews, 'messages': listMessages})
            return Response({'success': True, 'data': context})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Obtiene numero de notificaciones de un usuario
    @list_route(methods=['get'])
    def getCountNotifications(self, request):
        try:
            user = request.user
            profile = viewsProfiles.getProfile(user)
            count = Conversation.countNotifications(profile)
            return Response({'success': True, 'count': count})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Leido de conversacion
    @list_route(methods=['post'])
    def reviewConversation(self, request):
        try:
            user = request.user
            idProfile = viewsProfiles.getProfile(user).id
            idConversation = request.data.get('conversation', None)
            Conversation.addReview(idProfile, idConversation)
            return Response({'success': True, 'msg': 'conversation-review'})
        except Exception as e:
            if hasattr(e, 'message'):
                err = e.message
            else:
                err = e
            return Response({'success': False, 'err': str(err)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
