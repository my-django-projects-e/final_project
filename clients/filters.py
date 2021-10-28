import django_filters
from django_filters import CharFilter
from django.forms import TextInput

from .models import Client, Case


class ClientFilter(django_filters.FilterSet):
    policy_num = CharFilter(
        field_name="policy_num",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по полису",
    )
    full_name = CharFilter(
        field_name="full_name",
        lookup_expr="contains",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по ФИО",
    )
    company = CharFilter(
        field_name="company",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по компании",
    )
    policy_start_date = CharFilter(
        field_name="policy_start_date",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по старту полиса",
    )
    policy_end_date = CharFilter(
        field_name="policy_end_date",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по концу полиса",
    )


class CaseFilter(django_filters.FilterSet):
    num_case = CharFilter(
        field_name="num_case",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по полису",
    )
    case_start_date = CharFilter(
        field_name="case_start_date",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по старту полиса",
    )
    case_end_date = CharFilter(
        field_name="case_end_date",
        lookup_expr="startswith",
        widget=TextInput(attrs={"class": "form-control"}),
        label="Поиск по концу полиса",
    )
