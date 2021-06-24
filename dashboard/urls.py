from django.urls import path
from .views.rooms import ListRoomView, CreateRoomView, GetRoomView

urlpatterns = [
    path('rooms/', ListRoomView.as_view()),
    path('rooms/create', CreateRoomView.as_view()),
    path('rooms/<str:pk>', GetRoomView.as_view())
]
