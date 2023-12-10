# from django.urls import path
#
# from ads.views import AdCreateAPIView, AdListAPIView, AdUpdateAPIView, \
#     AdDestroyAPIView, AdRetrieveAPIView, \
#     CommentListCreateAPIView, CommentUpdateAPIView, CommentDestroyAPIView
#
# app_name = 'ads'

# urlpatterns = [
#     path('create/', AdCreateAPIView.as_view(), name='create_ad'),
#     path('', AdListAPIView.as_view(), name='ads_list'),
#     path('<int:pk>', AdRetrieveAPIView.as_view(), name='ad_retrieve'),
#     path('update/<int:pk>/', AdUpdateAPIView.as_view(), name='ad_update'),
#     path('destroy/<int:pk>/', AdDestroyAPIView.as_view(), name='ad_delete'),
#
#     path('comment/<int:ad_pk>/', CommentListCreateAPIView.as_view(),
#          name='comment_create'),
#     path('comment/update/<int:pk>/', CommentUpdateAPIView.as_view(),
#          name='comment_update'),
#     path('comment/destroy/<int:pk>/', CommentDestroyAPIView.as_view(),
#          name='comment_delete'),
#
# ]
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from ads.apps import SalesConfig
from ads.views import AdViewSet, CommentViewSet, UserAdsListView
from rest_framework_nested import routers

app_name = SalesConfig.name

router = routers.SimpleRouter()
router.register(r'ads', AdViewSet)

comments_router = routers.NestedSimpleRouter(router, r'ads', lookup='ads')
comments_router.register(r'comments', CommentViewSet, basename='ads-comments')

urlpatterns = [
    path('api/ads/me/', UserAdsListView.as_view(), name='ads_user_list'),
    path('api/', include(router.urls)),
    path('api/', include(comments_router.urls)),

]
