from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.exceptions import PermissionDenied

from events.models import Event
from babies.models import Baby
from events.serializers import EventSerializer

from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory

def evaluate_user(user, obj, request):
    return user.username == obj.baby.parent.username

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': evaluate_user,
                    'destroy': evaluate_user,
                    'update': evaluate_user,
                    'partial_update': evaluate_user,
                    'perform_create': evaluate_user,
                }
            }
        ),
    )

    #POST method    
    def perform_create(self, serializer):
        user = self.request.user
        # Check if parent owns baby (by id in request)
        baby = Baby.objects.get(pk=self.request.data['baby'])
        print(baby.parent.username != user.username)
        
        if(baby.parent.username != user.username):
            raise PermissionDenied('This is not your baby')
        else:
            event = serializer.save()
            assign_perm('events.change_event', user, event)
            assign_perm('events.view_event', user, event)
            return Response(serializer.data)
        
        
