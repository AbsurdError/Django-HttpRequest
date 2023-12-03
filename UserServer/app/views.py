from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']

    return HttpResponse(f'<h2>Host: {host}<br>User-agent: {user_agent}<br>IP client: {ip}</h2>')

def error(request):
    return HttpResponse('<h1>К сожалению произошла ошибка</h1>', status=400, reason='Incorrect data')

def user(request, login='Undefined', name_folder='Undefined', number_post=0):
    return HttpResponse(f'<h2>Логин: {login}<br>Имя папки: {name_folder}<br>Номер поста: {number_post}</h2>')
