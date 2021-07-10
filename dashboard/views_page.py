from django.http import JsonResponse


def home(request):
    message = {
        "message":"Welcome to Hotel Management System API, the following are the endpoints",
        "endpoints":[
            "api/v1/rooms/",
            "api/v1/rooms/create",
            "api/v1/rooms/<str:pk >",
            "api/v1/receptionist",
            "ap1/v1/auth/register",
            "api/v1/auth/login",
            "api/v1/swagger/[name= 'schema-swagger-ui']",
            "api/v1/redoc/[name = 'schema-redoc']"
        ]
    }
    return JsonResponse(message)
