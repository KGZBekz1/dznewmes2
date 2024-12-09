from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'GET':
        return HttpResponse('hi TUNES')

def emoji (request):
    if request.method == 'GET':
        return HttpResponse('🎄🏆 ')

def image_proger_view(request):
    return HttpResponse('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfl2CD8o7yQCJYk91VimvyGT0DJ8atwVtH-A&s')
