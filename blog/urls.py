from django.conf.urls import url
from .views import view_blog, article_detail

# If there are more app in one project with same url
app_name = "articles"

urlpatterns = [
    url(r'^$', view_blog, name='view_blog'),
    # Create nam capturing group
    # \w contains everything
    # https://youtu.be/c2hbT0uIcOQ
    url(r'^(?P<slug>[\w-]+)/$', article_detail, name="detail")
]
