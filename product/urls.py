from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^goods_list/$', views.GoodsListView.as_view(), name='list'),
    url(r'^goods_detail/(?P<goods_id>\d+)/$', views.GoodsDetailView.as_view(), name='detail'),
]