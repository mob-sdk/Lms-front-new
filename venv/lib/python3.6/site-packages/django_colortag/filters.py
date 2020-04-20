import django_filters

from .fields import ColortagChoiceField


class ColortagChoiceFilter(django_filters.ModelMultipleChoiceFilter):
    field_class = ColortagChoiceField
