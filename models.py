from django.db import models

class Tag(models.Model):
	name = models.CharField(max_length = 50)
	creation_time = models.DateTimeField(auto_now_add = True)
	modified_time = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name.encode('utf-8')

class Article(models.Model):
	title = models.CharField(max_length = 50)
	content = models.TextField(max_length = 20000)
	creation_time = models.DateTimeField(auto_now_add = True)
	modified_time = models.DateTimeField(auto_now = True)
	enable_comments = models.BooleanField(default = True)
	is_flatpage = models.BooleanField(default = False)
	flatpage_url = models.CharField(blank = True,max_length = 50)

	def __str__(self):
		return self.title.encode('utf-8')

class Comment(models.Model):
	visitor_name = models.CharField(max_length = 50)
	visitor_email = models.CharField(max_length = 50)
	visitor_site = models.CharField(max_length = 50)
	content = models.TextField(max_length = 20000)
	creation_time = models.DateTimeField(auto_now_add = True)
	article = models.ForeignKey('Article')

	def __str__(self):
		return self.visitor_name.encode('utf-8')+":"+(self.content)[0:15].encode('utf-8')

class Article_Tag(models.Model):
	article = models.ForeignKey('Article')
	tag = models.ForeignKey('Tag')

	def __str__(self):
		return '['+self.tag.name.encode('utf-8')+']-'+self.article.title.encode('utf-8')
