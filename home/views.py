from django.shortcuts import render
from home.models import Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {"categories": category_list}
    return render(request, 'home/index.html', context=context_dict)


def about(request):
    cat = {'cat': "cat"}
    return render(request, 'home/about.html', context=cat)
