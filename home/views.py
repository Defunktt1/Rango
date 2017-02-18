from django.shortcuts import render
from home.models import Category, Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {"categories": category_list}
    return render(request, 'home/index.html', context=context_dict)


def about(request):
    cat = {'cat': "cat"}
    return render(request, 'home/about.html', context=cat)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'home/category.html', context=context_dict)
