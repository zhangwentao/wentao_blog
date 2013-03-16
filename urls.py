from django.conf.urls.defaults import patterns, include, url
from views import article_list, article

urlpatterns = patterns('',
	(r'^article/list/(\d+)$',article_list),
	(r'^article/(\d+)$',article),
)
