from django.conf.urls import url
from home import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^home', views.index, name='index'),
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^about/', views.about, name='about'),
]
