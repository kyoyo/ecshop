from django.shortcuts import render
from django.views.generic import DetailView,ListView,TemplateView,FormView
from . import cart as cart_app
from .forms import CartForm
from product.models import Goods
from django.views.generic import ListView,DetailView
from .models import Cart,Item
from django.conf import settings

# Create your views here.


# class CartDetailView(DetailView):
#     model = Cart
#     template_name = 'order/shopcart.html'
#     pk_url_kwarg =
#
#     def get_context_data(self, **kwargs):
#
#         return super(CartDetailView, self).get_context_data(**kwargs)
#
#     def get_queryset(self):
#         pass

class CartGoodsView(ListView):
    template_name = 'order/shopcart.html'
    context_object_name = 'cart_item_list'

    def get_queryset(self):
        cart_item_list = []
        cart_id = self.request.session.get(settings.CART_ID)

        cart = Cart.objects.get(id=cart_id)
        item_list = Item.objects.filter(cart = cart)

        
        for item in item_list:
            goods_id = item.object_id
            quantity = item.quantity
            unit_price = item.unit_price
            goods = Goods.objects.get(id = goods_id)
            amount = unit_price * quantity
            goods.__setattr__('quantity',quantity)
            goods.__setattr__('amount',amount)
            goods.__setattr__('unit_price',unit_price)

            cart_item_list.append(goods)

        return cart_item_list
    
    def get_context_data(self, **kwargs):

        # summary = cartapp.summary()
        # kwargs['summary'] = summary
        
        return super(CartGoodsView, self).get_context_data(**kwargs)
        
        


# class AddToCartView(TemplateView):
#     template_name = 'order/addToCart.html'

class CartFormView(FormView):
    template_name = 'product/goods_detail.html'
    form_class = CartForm
    success_url = '/cart/addToCartSuccess/'

    def form_invalid(self, form):
        print("form_invalid")


    def form_valid(self, form):
        goods_id = self.kwargs['goods_id']
        goods = Goods.objects.get(id = int(goods_id))

        quantity = form.cleaned_data['quantity']

        cart = cart_app.Cart(self.request)
        cart.add(product = goods,unit_price = goods.price,quantity = quantity)
        
        return super(CartFormView, self).form_valid(form)




class PayDetailView(TemplateView):
    template_name = 'order/pay.html'


class AddToCartSuccessView(TemplateView):
    template_name = 'order/addToCart.html'


class SuccessView(TemplateView):
    template_name = 'order/success.html'