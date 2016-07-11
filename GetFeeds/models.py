from django.db import models
import json
from django.contrib.auth.models import User


class News(models.Model):
    user = models.ForeignKey(User, related_name='profile')
#    user = models.ForeignKey(User, unique=True, related_name='profile')
    headline = models.CharField(null=False, max_length=100)
    content = models.CharField(default="", max_length=5000)
    tags = models.CharField(default={}, max_length=200)
    source = models.CharField(default="", max_length=50)
    image = models.CharField(default="", max_length=150)

    def settags(self, x):
        self.tags = json.dumps(x)

    def gettags(self, x):
        return json.loads(self.tags)

    def __str__(self):
        return self.headline
