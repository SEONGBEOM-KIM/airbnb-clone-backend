from rest_framework.serializers import ModelSerializer
from users.serializers import TinyUserSerializer
from .models import Perk, Experience


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceSerializer(ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    perk = PerkSerializer(read_only=True, many=True)

    class Meta:
        model = Experience
        fields = (
            "name",
            "country",
            "city",
            "price",
            "address",
            "start",
            "end",
            "description",
            "host",
            "category",
            "perk",
        )
