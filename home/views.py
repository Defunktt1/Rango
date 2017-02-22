from django.shortcuts import render, render_to_response
from home.models import Category, Page
from home.forms import CategoryForm, PageForm
from django.template import RequestContext


def index(request):
    category_list = Category.objects.order_by('-likes')[:10]
    top_pages = Page.objects.order_by('-views')[:5]
    context_dict = {"categories": category_list,
                    "pages": top_pages}
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


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid:
            form.save(commit=True)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, 'home/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
            return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'home/add_page.html', context=context_dict)
