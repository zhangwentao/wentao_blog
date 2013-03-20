from django.conf.urls.defaults import patterns, include, url
from views import article_list, article, comment, code, home

urlpatterns = patterns('',
	('^$',home),
	(r'^article/list/(\d+)$',article_list),
	(r'^article/(\d+)$',article),
	(r'^article/comment$',comment),
	(r'^code/$',code)
)
