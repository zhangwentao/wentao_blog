from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
	('^$',views.article_list),
	(r'^article/list/$',views.article_list),
	(r'^article/list/(?P<page_num>\d+)$',views.article_list),
	(r'^article/$',views.article),
	(r'^article/(?P<article_id>\d+)$',views.article),
	(r'^article/comment$',views.comment),
	(r'^page/(?P<page_url>\w+)/$',views.page),
	(r'^captcha/$',views.captcha),
	(r'^feeds/$',views.BlogFeed()),
	(r'^feed/$',views.BlogFeed())
)

