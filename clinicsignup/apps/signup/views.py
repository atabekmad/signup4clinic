from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import *


def index(request):

        if request.method == 'POST':
                form = SignupForm(request.POST)
                if form.is_valid():
                        return HttpResponse("Success!!")
        else:
                form = SignupForm()

        return render(request,'signup/form.html',{'form':form})
            








