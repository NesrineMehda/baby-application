from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ActivitySerializer
from .models import Activity


@api_view(['GET'])
def getActivities(request):
    activities = Activity.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getActivity(request, pk):
    activity = Activity.objects.get(id=pk)
    serializer = ActivitySerializer(activity, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createActivity(request):
    serializer = ActivitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def activityUpdate(request, pk):
    activity = Activity.objects.get(id = pk)
    serializer = ActivitySerializer(instance=activity, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
