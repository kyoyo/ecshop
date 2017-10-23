from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Category,Goods
from django.conf import settings

# Create your views here.

class CategoryDetailView(ListView):
    template_name = 'product/goods_list.html'
    context_object_name = 'goods_list'

    page_type = ''
    paginate_by = settings.PAGINATE_BY
    page_kwarg = 'page'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        orderBy = self.request.GET.get('orderBy')

        category = Category.objects.get(pk=category_id)

        if orderBy == 'SALES_COUNT':
            goods_list = Goods.objects.filter(category=category).order_by('-sales_count')
        elif orderBy == 'PRICE':
            goods_list = Goods.objects.filter(category=category).order_by('price')
        else:
            goods_list = Goods.objects.filter(category=category)

        return goods_list

    def get_context_data(self, **kwargs):
        kwargs['category_id'] = self.kwargs['category_id']

        return super(CategoryDetailView, self).get_context_data(**kwargs)


class GoodsDetailView(DetailView):
    template_name = 'product/goods_detail.html'
    model = Goods
    pk_url_kwarg = 'goods_id'
    context_object_name = 'goods'

