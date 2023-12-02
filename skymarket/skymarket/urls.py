from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from users.views import UserActivationView

urlpatterns = [
                  path("api/admin/", admin.site.urls),
                  path("api/redoc-tasks/", include("redoc.urls")),
                  path("users/", include("users.urls")),
                  path("ads/", include("ads.urls")),
                  path('api/token/', TokenObtainPairView.as_view()),
                  path('api/refresh/', TokenRefreshView.as_view()),

                  path('auth/users/activate/<str:uid>/<str:token>/',
                       UserActivationView.as_view(), name='activation'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
