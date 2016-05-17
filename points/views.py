from django.db.models import Sum
from points.models import Point, Alias
from points.serializers import PointSerializer, DashboardSerializer, AliasSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.response import Response


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if "person" in self.request.query_params:
            self.queryset = self.queryset.filter(person__pk=self.request.query_params["person"])

        return super(PointViewSet, self).get_queryset()


class AliasViewSet(viewsets.ModelViewSet):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if "person" in self.request.query_params:
            self.queryset = self.queryset.filter(person__pk=self.request.query_params["person"])

        return super(AliasViewSet, self).get_queryset()


class MockService(viewsets.ReadOnlyModelViewSet):
    serializer_class = DashboardSerializer

    def list(self, request, *args, **kwargs):
        raise APIException(detail="list")
        return super(MockService, self).list(request, *args, **kwargs)


class DashboardViewSet(viewsets.ModelViewSet):
    serializer_class = DashboardSerializer

    def get_queryset(self):
        return User.objects.values("pk")\
            .annotate(total_points=Sum("points__amount"))\
            .order_by("-total_points")
