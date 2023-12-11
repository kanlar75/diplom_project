import django_filters

from ads.models import Ad


class AdFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name='title',
                                      lookup_expr='icontains',
                                      label='Filter ads by title containing '
                                            'the specified text.')

    class Meta:
        model = Ad
        fields = ('title',)
