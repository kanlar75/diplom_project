from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend

from .filters import AdFilter
from .models import Ad, Comment
from .paginators import AdPaginator
from .permissions import IsOwner, IsAdmin
from .serializers import AdSerializer, CommentSerializer, AdDetailSerializer


class AdViewSet(ModelViewSet):
    """ ViewSet объявления """

    default_serializer = AdSerializer
    queryset = Ad.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    serializer_class = AdSerializer
    serializer_classes = {
        "retrieve": AdDetailSerializer
    }
    pagination_class = AdPaginator

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer)

    def perform_create(self, serializer):
        """ Создание нового объявление и установка автора """

        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """ Обновление (редактирование) объявления """

        serializer.save(user=self.request.user)

    def get_permissions(self):
        """ Определяет права доступа в зависимости от выполняемого действия """

        if self.action in ['retrieve', 'create']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['destroy', 'update', 'partial_update']:
            permission_classes = [IsOwner | IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    """ ViewSet комментария """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        """ Получаем комментарии по id объявления """

        ad_id = self.kwargs['ads_pk']
        return Comment.objects.filter(ad_id=ad_id)

    def perform_create(self, serializer):
        """ Сохраняем пользователя, добавившего комментарий """

        ad_id = self.kwargs['ads_pk']
        ad = Ad.objects.get(pk=ad_id)
        serializer.save(ad=ad, user=self.request.user)

    def perform_update(self, serializer):
        """ Обновление комментария """

        serializer.save(user=self.request.user)

    def get_permissions(self):
        """ Определяет права доступа в зависимости от выполняемого действия """

        if self.action in ['retrieve', 'create']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['destroy', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class UserAdsListView(generics.ListAPIView):
    """ Представление списка объявлений пользователя """

    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        if self.request.user.role == 'admin':
            return Ad.objects.all()
        return Ad.objects.filter(user=self.request.user)

