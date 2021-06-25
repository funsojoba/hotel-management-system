from django.urls import path
from .views.rooms import ListRoomView, CreateRoomView, GetRoomView
from .views.receptionist import ReceptionistView

urlpatterns = [
    path('rooms/', ListRoomView.as_view()),
    path('rooms/create', CreateRoomView.as_view()),
    path('rooms/<str:pk>', GetRoomView.as_view()),
    path('receptionist', ReceptionistView.as_view())

]
