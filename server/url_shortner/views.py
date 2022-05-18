from operator import truediv
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UrlSerializer 
from rest_framework import status
from .serializers import UrlSerializer
from .models import URL
import random

# Create your views here.

class UrlList (APIView):
    def get(self, request, format = None):
        urls = URL.objects.all()
        serializer = UrlSerializer(urls,  many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        data = request.data
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!*^$-_"
        shorturl = ("".join(random.sample(s, 6)))
        data['url_short'] = shorturl
        serializer = UrlSerializer(data = data)
        longurl = data['url_original']
        shorturl = "http://127.0.0.1:8000/url/"+ shorturl
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id'],'original_url':longurl,'url_short':shorturl}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class UrlInd (APIView):
    def get(self,request, shorturl, format= None):
        try:
            link = self.get_object(shorturl)
            serializer = UrlSerializer(link)
            return redirect(serializer.data["url_original"])
        except:
            return redirect('http://localhost:3000/')

