from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homePage_main(request):
    return HttpResponse('main home page1 check!')
    