import django_filters
from .models import Ad


class MyModelFilter(django_filters.rest_framework.FilterSet):
    find = django_filters.CharFilter(field_name="title",
                                     lookup_expr="icontains", )

    class Meta:
        model = Ad
        fields = ("title", 'description', )
