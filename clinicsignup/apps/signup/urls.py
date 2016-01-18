from django.conf.urls import url
from . import views


app_name = 'signup'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^luck/$', views.luck, name='luck'),
    url(r'^disabled/$', views.disabled, name="disabled"),
]
