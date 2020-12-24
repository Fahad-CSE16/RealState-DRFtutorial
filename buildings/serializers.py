from rest_framework import serializers
from .models import Home, ImageFiles
class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields=('title','slug','photo','bathrooms','bedrooms','sqft','state','zipcode','address','city','sale_type','home_type','price')
class HomeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields='__all__'
        lookup_field='slug'
class ImageFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageFiles
        fields='__all__'
        lookup_field='home'
