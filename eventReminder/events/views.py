from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import eventDetail, eventTime

from .serializers import eventsSerializer


# Create your views here.


@api_view(['GET'])
def event_list(request):
    if request.method == 'GET':
        objects = eventDetail.objects.all()
        mainDict = {}
        listelement = []
        for obj in objects:
            indexo = 0
            innerDict = {'id': obj.id, 'real_name': obj.realName, 'tz': obj.timeZone}
            timeobj = eventTime.objects.filter(eventDetail=obj)
            innerlist = []
            for individualtime in timeobj:
                indexi = 0
                nesteddict = {'start_time': individualtime.startTime, 'end_time': individualtime.endTime}
                innerlist.insert(indexi, nesteddict)
                indexi += 1
            innerDict['activity_period'] = innerlist
            listelement.insert(indexo, innerDict)
            indexo += 1
        mainDict['members'] = listelement
        return Response(mainDict)
