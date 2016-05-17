from django.contrib import auth
from django.contrib.auth.models import User
from points.models import Point, Alias
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("pk", "username", "email")


class AliasSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        validated_data.update({"created_by": self.context["request"].user})
        return super(AliasSerializer, self).create(validated_data)

    class Meta:
        model = Alias
        fields = ('pk', "text", "created_by")


class AliasChoiceField(serializers.ChoiceField, AliasSerializer):
    pass


class PointDisplaySerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    pk = serializers.IntegerField(read_only=True)

    display_name = serializers.CharField(read_only=True)

    assigned_by = UserSerializer(read_only=True)

    amount = serializers.IntegerField()

    def to_representation(self, instance):
        if instance.alias is not None:
            instance.display_name = instance.alias
        else:
            instance.display_name = instance.person
        return super(PointDisplaySerializer, self).to_representation(instance)

    class Meta:
        fields = ('pk', "amount", "assigned_by", "display_name", "comment")


class PointSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)

    person = serializers.PrimaryKeyRelatedField(read_only=False,
                                                queryset=auth.models.User.objects.all())

    alias = serializers.PrimaryKeyRelatedField(read_only=False,
                                               queryset=Alias.objects.all(),
                                               required=False)

    assigned_by = UserSerializer(read_only=True)

    amount = serializers.IntegerField()

    # alias = AliasChoiceField(choices=Alias.objects.all(), allow_blank=True, required=False)

    def to_representation(self, instance):
        return PointDisplaySerializer(instance).data

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

