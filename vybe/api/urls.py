from django.urls import path
from .views import RoomListView, CreateRoomView, GetRoom, JoinRoom, UserInRoom


urlpatterns = [
    path('rooms', RoomListView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),


]

