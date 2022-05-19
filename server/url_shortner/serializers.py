from rest_framework import serializers
from .models import URL

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('id', 'url_original', 'url_short')


