from django.urls import path
from rooms import views

urlpatterns = [
    path("", views.see_all_rooms),  # -> rooms/
    path("<int:room_pk>", views.see_one_room),  # -> rooms/1/
]
