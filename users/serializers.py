from rest_framework.serializers import ModelSerializer
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "id",
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )


class PublicUserSerializer(ModelSerializer):
    from rooms.serializers import UserRoomSerializer
    from reviews.serializers import ReviewSerializer

    rooms = UserRoomSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "avatar",
            "rooms",
            "reviews",
        )
