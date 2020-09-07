import django_filters
from django_filters import CharFilter, BooleanFilter

from .models import *


class UserFilter(django_filters.FilterSet):

    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label='Имя')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label='Фамилия')

    phone_number = CharFilter(field_name='phone_number', lookup_expr='icontains', label='Контактный номер')
    # or NumberFilter

    is_active = BooleanFilter(field_name='is_active', label='Активен')

    class Meta:
        model = User
        exclude = 'created_at', 'updated_at'


