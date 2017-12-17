from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import SignUp


def index(request):
    return HttpResponse('Ready to rock')

def signups(request):
	signups = SignUp.objects.all()
	args = {}
	args['signups'] = signups
	template = "signups.html"
	return render(request, template, args)