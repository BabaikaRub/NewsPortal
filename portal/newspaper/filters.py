from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Post
        fields = ('title', 'author', 'time_create', 'post_category')
