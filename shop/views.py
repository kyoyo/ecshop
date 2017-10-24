from django.views.generic import TemplateView,FormView
from django.http.response import HttpResponse
from django.views.generic import ListView,DetailView
from product.models import Category,Goods
from django.conf import settings
from django import forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class IndexView(ListView):
    template_name = 'shop/index.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        category_list = Category.objects.filter(sort__gt=0)

        return category_list





