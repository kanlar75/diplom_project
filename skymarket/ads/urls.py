from django.urls import path, include

from ads.apps import SalesConfig
from ads.views import AdViewSet, CommentViewSet, UserAdsListView
from rest_framework_nested import routers

app_name = SalesConfig.name

router = routers.SimpleRouter()
router.register(r'ads', AdViewSet)

comments_router = routers.NestedSimpleRouter(
    router, r'ads', lookup='ads'
)
comments_router.register(
    r'comments', CommentViewSet, basename='ads-comments'
)

urlpatterns = [
    path('ads/me/', UserAdsListView.as_view(), name='ads_user_list'),
    path('', include(router.urls)),
    path('', include(comments_router.urls)),

]

