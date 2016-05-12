from django.http import HttpResponse
from django.shortcuts import render
from points.models import Point
from points.serializers import PointSerializer
from rest_framework import viewsets


# Create your views here.
class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
