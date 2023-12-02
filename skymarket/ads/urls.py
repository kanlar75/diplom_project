from django.urls import path

from ads.views import AdCreateAPIView, AdListAPIView, AdUpdateAPIView, AdDestroyAPIView, AdRetrieveAPIView, \
    CommentListCreateAPIView, CommentUpdateAPIView, CommentDestroyAPIView

app_name = 'ads'


urlpatterns = [
    path('create/', AdCreateAPIView.as_view(), name='create_ad'),
    path('view/', AdListAPIView.as_view(), name='ads_list'),
    path('view/<int:pk>', AdRetrieveAPIView.as_view(), name='ad_retrieve'),
    path('update/<int:pk>/', AdUpdateAPIView.as_view(), name='ad_update'),
    path('destroy/<int:pk>/', AdDestroyAPIView.as_view(), name='ad_destroy'),

    path('comment/<int:ad_pk>/', CommentListCreateAPIView.as_view(), name='create_ad'),
    path('comment/update/<int:pk>/', CommentUpdateAPIView.as_view(), name='ad_update'),
    path('comment/destroy/<int:pk>/', CommentDestroyAPIView.as_view(), name='ad_destroy'),

]