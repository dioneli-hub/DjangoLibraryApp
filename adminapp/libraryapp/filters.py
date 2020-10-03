import django_filters
from django_filters import CharFilter, BooleanFilter, ChoiceFilter

from .models import *


class UserFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label='Имя')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label='Фамилия')
    phone_number = CharFilter(field_name='phone_number', lookup_expr='icontains', label='Контактный номер')
    is_active = ChoiceFilter(field_name='is_active', label='Статус', choices=((True, 'Активный'),
                                                                              (False, 'Неактивный')))

    class Meta:
        model = User
        exclude = 'created_at', 'updated_at'
