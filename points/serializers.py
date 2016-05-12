from points.models import Point
from rest_framework.serializers import *


class PointSerializer(ModelSerializer):
    pk = IntegerField(read_only=True)
    points = IntegerField()

    class Meta:
        model = Point
        fields = ('pk', 'points')
