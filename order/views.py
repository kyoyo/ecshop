from django.shortcuts import render
from django.views.generic import DetailView,ListView,TemplateView,FormView
from .cart import CartManager
from .forms import CartForm
from product.models import Goods
from django.views.generic import ListView,DetailView
from .models import Cart,Item
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.


class CartGoodsView(ListView):
    template_name = 'order/shopcart.html'
    context_object_name = 'cart_item_list'

    def get_queryset(self):

        item_list = Item.objects.filter(cart=CartManager(self.request).cart)

        return item_list
    
    def get_context_data(self, **kwargs):
        summary = CartManager(self.request).summary()
        kwargs['summary'] = summary
        
        return super(CartGoodsView, self).get_context_data(**kwargs)
        

class CartFormView(FormView):
    template_name = 'product/goods_detail.html'
    form_class = CartForm


    def form_invalid(self, form):
        print("form_invalid")

    def form_valid(self, form):
        goods_id = self.kwargs['goods_id']
        goods = Goods.objects.get(id = int(goods_id))

        quantity = form.cleaned_data['quantity']

        cart = CartManager(self.request)
        cart.add(product = goods,unit_price = goods.price,quantity = quantity)

        return HttpResponseRedirect(reverse('order:addToCartSuccess',kwargs={'goods_id':goods_id}))


class PayDetailView(TemplateView):
    template_name = 'order/pay.html'


class AddToCartSuccessView(TemplateView):
    template_name = 'order/addToCart.html'

    def get_context_data(self, **kwargs):
        context = super(AddToCartSuccessView, self).get_context_data(**kwargs)
        goods = Goods.objects.get(id = int(self.kwargs['goods_id']))
        context['goods'] = goods

        return context



class SuccessView(TemplateView):
    template_name = 'order/success.html'