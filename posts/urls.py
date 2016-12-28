"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from posts import views
from posts.views import PostList, PostCreate, PostDetail, Index
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', Index.as_view()),
   	url(r'^$', PostList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', PostDetail.as_view()),
   	url(r'^create/$', PostCreate.as_view()),
   	url(r'^update/$', views.post_update),
   	url(r'^delete/(?P<pk>[0-9]+)/$', views.DeletePost, name="DeletePost"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
