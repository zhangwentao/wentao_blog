# coding:utf-8
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from models import Article,Tag,Article_Tag,Comment

def article_list( request,page_num ):
	all_article_list = Article.objects.order_by("-creation_time")
	page_num = int( page_num )
	paging_step = 5 
	paging = Paginator( all_article_list, paging_step )
	article_list_page = paging.page( page_num )
	pre_page = page_num-1 if article_list_page.has_previous() else ''
	next_page = page_num+1 if article_list_page.has_next() else ''
	return render_to_response('blog_abstract_list.html',{'article_list':article_list_page.object_list,'next_page':next_page,'pre_page':pre_page,'cur_page':page_num})
