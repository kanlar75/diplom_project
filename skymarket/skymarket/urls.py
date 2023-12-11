from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path("api/admin/", admin.site.urls),
                  path("api/redoc-tasks/", include("redoc.urls")),

                  path("api/", include('users.urls')),
                  path('api/', include('ads.urls')),

                  path('api/token/', TokenObtainPairView.as_view(),
                       name='token_obtain_pair'),
                  path('api/refresh/', TokenRefreshView.as_view(),
                       name='token_refresh'),

                  path('api/swagger/',
                       schema_view.with_ui('swagger', cache_timeout=0),
                       name='schema-swagger-ui'),
                  path('api/redoc/',
                       schema_view.with_ui('redoc', cache_timeout=0),
                       name='schema-redoc'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
