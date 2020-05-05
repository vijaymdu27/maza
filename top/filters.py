from .models import ApiVieu
import django_filters


class ApiVieuFilters(django_filters.FilterSet):
    class Meta:
        model = ApiVieu
        fields = ['title' , 'location']