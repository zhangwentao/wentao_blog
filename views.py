# coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.paginator import Paginator
from models import Article,Tag,Article_Tag,Comment
from DjangoVerifyCode import Code
import re
from django.contrib.syndication.views import Feed 
from django.utils.safestring import mark_safe
import markdown

def article_list( request,page_num='1' ):
	all_article_list = Article.objects.filter(is_flatpage=False).order_by("-creation_time")
	page_num = int( page_num )
	paging_step = 5
	paging = Paginator( all_article_list, paging_step )
	article_list_page = paging.page( page_num )
	pre_page = page_num-1 if article_list_page.has_previous() else ''
	next_page = page_num+1 if article_list_page.has_next() else ''
	return render_to_response('blog/abstract_list.html',{'article_list':article_list_page.object_list,'next_page':next_page,'pre_page':pre_page,'cur_page':page_num})

def captcha( request ):
	code = Code(request)
	code.type = 'number'
	code.img_width = 120
	code.img_height = 70
	return code.display()

def article( request, article_id='null', template='blog/article_page.html' ):
	if article_id == 'null':
		article = Article.objects.filter(is_flatpage=False).order_by("-creation_time")[0]
	else:
		article = Article.objects.get( id = article_id )
	comment_list = Comment.objects.filter( article = article )
	context_instance = RequestContext(request)
	param_dict = {
			'article':article,
			'comment_list':comment_list,
			'page_url':request.build_absolute_uri(),
			}
	return render_to_response( template, param_dict, context_instance)

def validateEmailAddr(addrString):
	pattern = re.compile("\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*")	
	result = re.search(pattern,addrString)
	if result == None:
		return False
	else:
		return True 

def comment(request):
	post = request.POST
	article_id = post['artical_id']
	name = post['name']
	email = post['email']
	site = post['site']
	content = post['content']
	veri_code = post['veri_code']
	page_url=post['page_url']
	code = Code(request)
	if name == '' or email == '' or content == '':
		return error("姓名、邮箱和内容是必填的。")
	if validateEmailAddr(email) == False:
		return error("你的邮箱地址的格式不对。")
	if veri_code == '':
		return error("请填写验证码")
	if not code.check(veri_code):
		return error("验证码不正确")
	article=Article.objects.get(id = article_id)
	com = Comment(visitor_name=name,visitor_email=email,visitor_site=site,content=content,article = article)
	com.save()
	return HttpResponseRedirect(page_url)

def page(request,page_url):
	print page_url
	page_article = Article.objects.filter(is_flatpage=True).get(flatpage_url = page_url)
	return article(request,page_article.id,'blog/flatpage.html') 

def error(reason):
	return render_to_response("blog/error.html",{"reason":reason})

def handle404(request):
	return error("404 你懂的")

def handle500(request):
	return error("500 你懂得")

class BlogFeed(Feed):
	title = "文韬的BLOG"
	link = 'http://wentao.me'
	description = "wentao's blog"	
	def items(self):
		return Article.objects.filter(is_flatpage=False).order_by("-creation_time")
	def item_title(self,item):
		return item.title
	def item_link(self,item):
		return self.link+'/blog/article/'+str(item.id)
	def item_description(self,item):
		return mark_safe(markdown.markdown(item.content))
	def item_pubdate(self,item):
		return item.modified_time
