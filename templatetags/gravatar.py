from django import template
import md5
register = template.Library()

def gravatar_url(email_addr,avatar_width):
	prifix = 'http://www.gravatar.com/avatar/'
	suffix = '?'+avatar_width
	md5_str = md5.new(email_addr).hexdigest()
	avatar_url = prifix+md5_str+suffix
	return avatar_url

register.filter('gravatar', gravatar_url)
