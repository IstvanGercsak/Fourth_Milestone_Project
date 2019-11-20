from django.conf.urls import url
from .views import view_blog

urlpatterns = [
    url(r'^$', view_blog, name='view_blog'),
]