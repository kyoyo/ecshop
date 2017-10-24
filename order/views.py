from django.shortcuts import render
from django.views.generic import DetailView,ListView,TemplateView,FormView
from cart.models import Cart,Item
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

class CartDetailView(TemplateView):
    template_name = 'order/shopcart.html'

# class AddToCartView(TemplateView):
#     template_name = 'order/addToCart.html'

# class CartFormView(FormView):
#     template_name = 'order/shopcart.html'


class PayDetailView(TemplateView):
    template_name = 'order/pay.html'


class SuccessView(TemplateView):
    template_name = 'order/success.html'
