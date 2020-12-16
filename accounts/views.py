from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer

@api_view(['POST',])
def register_view(request):
    if request.method=="POST":
        serializer=RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user=serializer.save()
            data['response']="Successfully done"
            data['username']=user.username
            data['email']=user.email
            data['first_name']=user.first_name
            data['last_name']=user.last_name
        else:
            data=serializer.errors
        return Response(data)



