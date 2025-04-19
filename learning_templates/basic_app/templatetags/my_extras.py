from django import template

register= template.Library()


#menyre poshte eshte dekorator per te rregjistruar funksionin
@register.filter(name='cut')
def cut(value, arg):
  """
  this cuts out all value of 'arg' from the string
  """
  
  return value.replace(arg,'')

#kjo eshte nje menyre per te rregjistruar funksionin
#register.filter('cut', cut)