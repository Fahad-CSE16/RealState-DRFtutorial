from rest_framework import permissions, serializers,status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Home, ImageFiles
from .serializers import HomeSerializer,HomeDetailSerializer,ImageFilesSerializer
class HomeListAPIView(ListAPIView):
    permission_classes=(permissions.AllowAny,)
    serializer_class=HomeSerializer
    queryset=Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field='slug'
class HomeDetailAPIView(RetrieveAPIView):
    serializer_class=HomeDetailSerializer
    queryset=Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field='slug'
class ImageView(APIView):
    def get(self,request,pk,format=None):
        home=Home.objects.get(pk=pk)
        images=home.images.all()
        serializer=ImageFilesSerializer(images,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
from django.db.models import Q, query
class Search(APIView):
    permission_classes=(permissions.AllowAny,)
    def post(self, request, format=None):
        data=self.request.data
        queryset=Home.objects.filter(is_published=True)
        try:
            str=data['str']
            q= (Q(description__icontains=str)) | (Q(title__icontains=str))
            queryset=queryset.filter(q)
        except:
            pass
        try:
            price_from=data['price_from']
            queryset=queryset.filter(price__gte=price_from)
        except:
            pass
        try:
            price_to=data['price_to']
            queryset=queryset.filter(price__lte=price_to)
        except:
            pass
        try:
            city=data['city']
            queryset=queryset.filter(city__iexact=city)
        except:
            pass
        serializer=HomeSerializer(queryset,many=True)
        return Response(serializer.data)
