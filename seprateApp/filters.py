from django.db.models import fields
import django_filters
from seprateApp.models import *
from django_filters import DateFilter
class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='create_at',lookup_expr='gte')
    end_date = DateFilter(field_name='create_at',lookup_expr='lte')
    class Meta:
        model = Order
        fields = "__all__"
        exclude = [ 'customer','create_at' ]