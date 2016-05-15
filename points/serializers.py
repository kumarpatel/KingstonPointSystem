from django.contrib import auth
from django.contrib.auth.models import User
from points.models import Point
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("pk", "username", "email")


class PointSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    person = serializers.SlugRelatedField(slug_field="username", read_only=False, queryset=auth.models.User.objects.all())
    assigned_by = serializers.SlugRelatedField(slug_field="username", read_only=True)
    amount = serializers.IntegerField()

    def create(self, validated_data):
        validated_data.update({"assigned_by": self.context["request"].user})
        return super(PointSerializer, self).create(validated_data)

    class Meta:
        model = Point
        fields = ('pk', "amount", "person", "assigned_by", "alias", "comment")


class UserSlugSerializer(serializers.SlugRelatedField, UserSerializer):
    pass


class DashboardSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def to_representation(self, instance):
        return {
            'person': UserSerializer(User.objects.get(pk=instance["pk"])).data,
            'points': 0 if instance["total_points"] is None else instance["total_points"]
        }

