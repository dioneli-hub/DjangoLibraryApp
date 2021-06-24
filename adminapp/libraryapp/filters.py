import django_filters
from django_filters import CharFilter, BooleanFilter, ChoiceFilter

from .models import *


class UserFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label='Name')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label='Surname')
    phone_number = CharFilter(field_name='phone_number', lookup_expr='icontains', label='Phone number')
    is_active = ChoiceFilter(field_name='is_active', label='Status', choices=((True, 'Active'),
                                                                              (False, 'Inactive')))

    class Meta:
        model = User
        exclude = 'created_at', 'updated_at'
