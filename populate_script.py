import os
import django
from home.models import Category, Page


def add_page(category, title, url, views=0):
    p = Page.objects.get_or_create(category=category, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "https://docs.python.org/3/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://korokithakis.net/turorials/python/"},
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.10/intro/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"},
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"},
    ]

    categories = {
        "Python": {"pages": python_pages},
        "Django": {"pages": django_pages},
        "Other Frameworks": {"pages": other_pages}
    }

    for category, category_data in categories.items():
        c = add_category(categories)
        for p in category_data["pages"]:
            add_page(c, p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {} - {}".format(str(c), str(p)))


if __name__ == "__main__":
    print("Starting app population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rango.settings')
    django.setup()
    populate()
