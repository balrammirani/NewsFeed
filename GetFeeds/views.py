from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView, RetrieveUpdateAPIView,CreateAPIView,DestroyAPIView
from rest_framework.response import Response
from .models import NewsFeed
from .serializer import NewsSerializer,NewsDetailSerializer, NewsUpdateSerializer
# Create your views here.


class NewsListAPIView(ListAPIView):

        queryset = NewsFeed.objects.all()
        serializer_class = NewsSerializer


class NewsDetailAPIView(RetrieveAPIView):

    queryset = NewsFeed.objects.all()
    serializer_class = NewsDetailSerializer


class NewsUpdateAPIView(RetrieveUpdateAPIView):

    queryset = NewsFeed.objects.all()
    serializer_class = NewsUpdateSerializer


class NewsDeleteAPIView(DestroyAPIView):

    queryset = NewsFeed.objects.all()
    serializer_class = NewsDetailSerializer


class NewsCreateAPIView(CreateAPIView):

    queryset = NewsFeed.objects.all()
    serializer_class = NewsDetailSerializer
