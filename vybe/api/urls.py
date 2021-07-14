from django.urls import path
from .views import RoomListView, CreateRoomView

urlpatterns = [
    path('room/', RoomListView.as_view()),
    path('create-room/', CreateRoomView.as_view()),

]
