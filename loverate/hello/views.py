from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Главная")

def about(request, name, age):
    return HttpResponse(f"""
    <h2>О человеке</h2>
    <p>Имя: {name}</p>
    <p>Возраст: {age}</p>
    """)

def contacts(request):
    return HttpResponse("Контакты")