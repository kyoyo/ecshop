from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^category/(?P<category_id>\d+)/$', views.CategoryDetailView.as_view(), name='category_detail'),
    url(r'^category/(?P<category_id>\d+)/page/(?P<page>\d+)/$',views.CategoryDetailView.as_view(), name='page'),
    url(r'^category/(?P<category_id>\d+)/goods_detail/(?P<goods_id>\d+)/$', views.GoodsDetailView.as_view(), name='detail'),

]