from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone

def landing(request):
    return render(request,'landing.html')
