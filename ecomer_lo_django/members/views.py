from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


# Create your views here.
def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

# def testing(request):
#     template3=loader.get_template('template.html')
#     context={'firstname':'enzo, de la funcion testing',
#     }
#     return HttpResponse(template3.render(context, request))
    
def mysecond(request):
    template2 = loader.get_template('mysecond.html')
    return HttpResponse(template2.render())

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())