from django.db import models

class Tag(models.Model):
	name = models.CharField(max_length = 50)
	creation_time = models.DateTimeField(auto_now_add = True)
	modified_time = models.DateTimeField(auto_now = True)

class Article(models.Model):
	title = models.CharField(max_length = 50)
	content = models.TextField(max_length = 20000)
	creation_time = models.DateTimeField(auto_now_add = True)
	modified_time = models.DateTimeField(auto_now = True)

class Comment(models.Model):
	visitor_name = models.CharField(max_length = 50)
	visitor_email = models.CharField(max_length = 50)
	visitor_site = models.CharField(max_length = 50)
	content = models.TextField(max_length = 20000)
	creation_time = models.DateTimeField(auto_now_add = True)
	article = models.ForeignKey('Article')

class Article_Tag(models.Model):
	article = models.ForeignKey('Article')
	tag = models.ForeignKey('Tag')
