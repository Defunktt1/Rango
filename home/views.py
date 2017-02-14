from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'home/index.html', context=context_dict)


def about(request):
    return HttpResponse("Page about my site")
