from django.urls import path
from .views import UrlList, UrlInd


urlpatterns = [
    path('', UrlList.as_view()),
    path('<str:shorturl>', UrlInd.as_view())
    ]
