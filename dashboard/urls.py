from django.urls import path
from .views.rooms import ListRoomView, CreateRoomView, GetRoomView
from .views.receptionist import ReceptionistView
from .views.register import RegisterView
from .views.login import LoginView

from .views_page import home

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views


schema_view = get_schema_view(
    openapi.Info(
        title="Hotel Management System API",
        default_version='v1',
        description="API for internal management of hotel activities",
        contact=openapi.Contact(email="hrfunsojoba@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', home),
    path('rooms/', ListRoomView.as_view()),
    path('rooms/create', CreateRoomView.as_view()),
    path('rooms/<str:pk>', GetRoomView.as_view()),
    path('receptionist', ReceptionistView.as_view()),
    path('auth/register', RegisterView.as_view()),
    path('auth/login', LoginView.as_view()),
    path('token/', views.obtain_auth_token),


    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
