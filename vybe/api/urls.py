from django.urls import path
from .views import RoomListView, CreateRoomView, GetRoom


urlpatterns = [
    path('rooms/', RoomListView.as_view()),
    path('create-room/', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),

]

