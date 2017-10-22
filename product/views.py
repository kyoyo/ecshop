from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Category,Goods
# Create your views here.

class GoodsListView(ListView):
    pass

class GoodsDetailView(DetailView):
    template_name = 'product/goods_detail.html'
    model = Goods
    pk_url_kwarg = 'goods_id'
    context_object_name = 'goods'

