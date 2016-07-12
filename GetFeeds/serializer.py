from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from users.serializers import UserDetailSerializer
from .models import News


class NewsSerializer(ModelSerializer):
    detail = HyperlinkedIdentityField(view_name='detail', lookup_field="pk")
    user = UserDetailSerializer(read_only=True)
    # user = SerializerMethodField()
    # image = SerializerMethodField()

    class Meta:
        model = News
        fields = [
            "user",
            "headline",
            "content",
            "source",
            "detail",
        ]

#    def get_user(self, obj):
#        return str(obj.user.username)
'''
    def get_image(self,obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image
'''


class NewsCreateSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = [
            "headline",
            "content",
            "tags",
            "source",
            "image"
        ]


class NewsDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = News
        fields = [
            "user",
            "headline",
            "content",
            "tags",
            "source",
            "image"
        ]
        read_only_fields = [
            "user",
            "tags",
            "source",
            "image",
        ]
        # fields = "__all__"

'''
class NewsUpdateSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = [
            "headline",
            "content",
            "tags",
            "source",
            # "image"
        ]
'''