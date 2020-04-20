from django.urls import path
from django.conf.urls import url

from course.urls import INSTANCE_URL_PREFIX, MODULE_URL_PREFIX, \
    USER_URL_PREFIX, EDIT_URL_PREFIX

from exercise.urls import EXERCISE_URL_PREFIX
from . import views
 
app_name = 'comments'
urlpatterns = [
    url(EXERCISE_URL_PREFIX+r'comment/(?P<post_pk>\d+)/$', views.comment, name='comment'),
]