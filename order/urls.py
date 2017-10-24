from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^cart/$', views.CartDetailView.as_view(), name='cart'),
    url(r'^pay/$', views.PayDetailView.as_view(), name='pay'),
    url(r'^addToCart.html$', TemplateView.as_view(template_name = 'order/addToCart.html'), name='addToCart'),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),
]