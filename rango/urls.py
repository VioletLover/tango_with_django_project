from django.conf.urls import url
from django.views.generic import ListView
from . import views
from .models import Page

# http://127.0.0.1:8000/rango/category/django/'http://www.djangorocks.com/
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$',views.about, name="about"),
    url(r'^add_category/$',views.add_category,name='add_category'),
    url(r'^category/(?P<category_name_slug>.+)/$',views.category,name="category"),
    url(r'^add_page/$',views.add_page,name='add_page'),
    url(r'^pages/$',ListView.as_view(template_name='rango/page_list.html',model=Page),name='page_list'),

]