from rest_framework import serializers
from .models import Blog

class BlogSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'