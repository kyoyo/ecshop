from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, FormView
from .cart import CartManager
from .forms import CartForm
from product.models import Goods
from django.views.generic import ListView, DetailView
from .models import Cart, Item
from django.conf import settings
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core.urlresolvers import reverse


# Create your views here.


class CartGoodsView(ListView):
    template_name = 'order/shopcart.html'
    context_object_name = 'cart_item_list'

    # def __init__(self):
    #     self.cart = CartManager.get_cart(self.request)

    def get_queryset(self):
        cart = CartManager.get_cart(self.request)
        item_list = Item.objects.filter(cart=cart)

        return item_list

    def get_context_data(self, **kwargs):
        cart = CartManager.get_cart(self.request)

        #total_price = self.cart.total_price()
        kwargs['cart'] = cart

        return super(CartGoodsView, self).get_context_data(**kwargs)


class CartFormView(FormView):
    template_name = 'product/goods_detail.html'
    form_class = CartForm

    def form_invalid(self, form):
        print("form_invalid")

    def form_valid(self, form):

        action = self.request.GET.get('action')

        goods_id = form.data['goods_id']
        quantity = form.cleaned_data['quantity']

        goods = Goods.objects.get(id=int(goods_id))

        cart = CartManager(self.request)

        if action == 'add':
            cart.add(product=goods, unit_price=goods.price, quantity=quantity)
            return HttpResponseRedirect(reverse('order:addToCartSuccess', kwargs={'goods_id': goods_id}))
        else:
            return HttpResponseRedirect(reverse('order:cart'))

    # def post(self, request, *args, **kwargs):
    #     cart = CartManager(self.request)
    #
    #     action = self.request.POST.get('action')
    #     item_id = self.request.POST.get('item_id')
    #     #goods_id = self.request.GET.get('goods_id')
    #     quantity = self.request.POST.get('quantity')
    #     item = Item.objects.get(id=item_id)
    #
    #     goods = Goods.objects.get(id=int(item.object_id))
    #
    #     data = {'quantity':quantity}
    #     if action == 'add':
    #         cart.add(product=goods, unit_price=goods.price, quantity=int(quantity))
    #         return JsonResponse(data)



    def get(self, request, *args, **kwargs):
        cart = CartManager(self.request)

        action = self.request.GET.get('action')
        item_id = self.request.GET.get('item_id')
        #goods_id = self.request.GET.get('goods_id')
        quantity = self.request.GET.get('quantity')
        item = Item.objects.get(id=item_id)

        goods = Goods.objects.get(id=int(item.object_id))

        if action == 'add':
            cart.add(product=goods, unit_price=goods.price, quantity=quantity)
            return HttpResponseRedirect(reverse('order:cart'))
        if action == 'delete':
            cart.remove_item(item_id)
            return HttpResponseRedirect(reverse('order:cart'))



    # def get_context_data(self, **kwargs):
    #     cart = CartManager.get_cart(self.request)
    #
    #     item_list = Item.objects.filter(cart=cart)
    #
    #     kwargs['cart_item_list'] = item_list
    #     kwargs['cart'] = cart
    #
    #     kwargs['redirect_to'] = reverse('order:cart')
    #
    #     return super(CartFormView, self).get_context_data(**kwargs)


class PayDetailView(TemplateView):
    template_name = 'order/pay.html'


class AddToCartSuccessView(TemplateView):
    template_name = 'order/addToCart.html'

    def get_context_data(self, **kwargs):
        context = super(AddToCartSuccessView, self).get_context_data(**kwargs)
        goods = Goods.objects.get(id=int(self.kwargs['goods_id']))
        context['goods'] = goods

        return context


class SuccessView(TemplateView):
    template_name = 'order/success.html'
