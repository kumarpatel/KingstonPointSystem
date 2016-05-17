from django.db.models import Sum
from points.models import Point, Alias
from points.serializers import PointSerializer, DashboardSerializer, AliasSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User


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


class DashboardViewSet(viewsets.ModelViewSet):
    serializer_class = DashboardSerializer

    def get_queryset(self):
        return User.objects.values("pk")\
            .annotate(total_points=Sum("points__amount"))\
            .order_by("-total_points")
