from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from babies.models import Baby
from events.models import Event
from babies.serializers import BabySerializer
from events.serializers import EventSerializer

from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory

def evaluate_user(user, obj, request):
    return user.username == obj.parent.username
    
class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
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
                    'events': evaluate_user
                }
            }
        ),
    )

    # POST method
    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('baby.change_baby', user, baby)
        assign_perm('baby.view_baby', user, baby)
        return Response(serializer.data)

    # GET method
    @action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        baby = self.get_object()
        queryset = Event.objects.filter(baby = baby)
        data = EventSerializer(queryset, many = True).data
        return Response(data)