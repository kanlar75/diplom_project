from django.urls import include, path, re_path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig

app_name = UsersConfig.name

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    # path('', include(users_router.urls)),
    path('v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
