from django.apps import AppConfig


class ColorTagConfig(AppConfig):
    name = 'django_colortag'
    verbose_name = 'Django Colortag'

    required_apps = ('js_jquery_toggle',)
