from django import template

register = template.Library()   
#@register.filter(name='cut')		#decorator 
def cut(value,arg):
 	return value.replace(arg,'')

register.filter('cut',cut)  #we can replace it with decorator @ in the above