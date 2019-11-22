from django.conf.urls import url
from .views import view_blog, article_detail

# If there are more app in one project with same url
app_name = "articles"

urlpatterns = [
    url(r'^$', view_blog, name='view_blog'),
    url(r'^(?P<slug>[\w-]+)/$', article_detail, name="detail")
]
