from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import *
from .models import Doctor


def luck(request):
    return render(request, 'signup/success.html')


def index(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('signup:luck'))
    else:
        form = SignupForm()

    doctor_list = Doctor.objects.all()
    return render(request,'signup/form.html',{'form':form, 'doctor_list' : doctor_list, 'post_data': request.POST})


def disabled(request):
    return HttpResponse("this is a return data")

