from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from .models import User
from rest_framework import status


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST',])
def registration_view(request):
    if request.method=='POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user=serializer.save()
            data['response']="successfully registrated"
            data['email']=user.email
            data['username']=user.username
            return Response(data)
        else:
            data = serializer.errors
            return Response(data)
