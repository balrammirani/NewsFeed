from rest_framework.serializers import ModelSerializer
from .models import NewsFeed


class NewsSerializer(ModelSerializer):

    class Meta:
        model = NewsFeed
        fields = ["headline", "content", "source"]


class NewsDetailSerializer(ModelSerializer):

    class Meta:
        model = NewsFeed
        fields = [
            "user",
            "headline",
            "content",
            "tags",
            "source",
            "image"
        ]


class NewsUpdateSerializer(ModelSerializer):

    class Meta:
        model = NewsFeed
        fields = [
            "headline",
            "content",
            "tags",
            "source",
           # "image"
        ]
