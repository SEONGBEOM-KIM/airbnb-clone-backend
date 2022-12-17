from django.contrib import admin
from .models import Room, Amenity

# action must include 3 pharameter
# model_admin -> which model use this action
# request -> information about user who request action
# queryset -> elements(object) you selected
@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
    )

    search_fields = (
        "name",
        "^price",  # 'No' means contian / '^' means startwith / '=' means exact
        "owner__username",
    )

    # def total_amenities(self, room): # room -> object
    #     return room.amenities.count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    # show created_at, updated_at in each amenity details
    readonly_fields = (
        "created_at",
        "updated_at",
    )
