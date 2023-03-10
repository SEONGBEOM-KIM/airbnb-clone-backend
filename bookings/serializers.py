from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Booking


class PublicBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )


class CreateExperienceBookingSerializer(ModelSerializer):
    experience_time = serializers.DateTimeField()

    class Meta:
        model = Booking
        fields = (
            "experience_time",
            "guests",
        )

    def validate_experience_time(self, value):
        now = timezone.localtime(timezone.now())
        if now > value:
            raise serializers.ValidationError("Can't book in the past")
        return value

    def validate(self, data):
        if Booking.objects.filter(experience_time=data["experience_time"]).exists():
            raise serializers.ValidationError("Those dates are already taken.")
        return data


class CreateRoomBookingSerializer(ModelSerializer):
    check_in = serializers.DateField()  # check_in was optional, so overide for required
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    def validate_check_in(self, value):  # validate_ <- customized validation
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value  # returning value -> is valid. or raise error

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate(self, data):
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError(
                "Check in should be smaller than check out."
            )
        if Booking.objects.filter(
            check_in__lte=data["check_out"],
            check_out__gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError(
                "Those (or some of those) dates are already taken."
            )
        return data
