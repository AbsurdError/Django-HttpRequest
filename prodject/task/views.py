from django.shortcuts import render
from django.http import HttpResponse

def error(request):
    return HttpResponse('К сожалению произошла ошибка', status=400, reason='Incorrect data')
