from django.views.generic import TemplateView,FormView
from django.http.response import HttpResponse
#from .forms import LoginForm,RegisterForm
from django.views.generic import ListView,DetailView
from product.models import Category,Goods
from django.conf import settings
from django import forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from django.core.exceptions import ObjectDoesNotExist


class ArticleListView(ListView):
    pass
    # template_name = 'app01/index.html'
    # #context_object_name = 'article_list'
    #
    # page_type = ''
    # paginate_by = settings.PAGINATE_BY
    # page_kwarg = 'page'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(ArticleListView, self).get_context_data(**kwargs)
    #     article_list = Article.objects.all()
    #     paginator = Paginator(article_list, 5)
    #     page = self.request.GET.get('page')
    #     try:
    #         article_list = paginator.page(page)
    #     except PageNotAnInteger:
    #         # If page is not an integer, deliver first page.
    #         article_list = paginator.page(1)
    #     except EmptyPage:
    #         # If page is out of range (e.g. 9999), deliver last page of results.
    #         article_list = paginator.page(paginator.num_pages)
    #     context['article_list'] = article_list
    #     return context


class IndexView(ListView):
    template_name = 'shop/index.html'
    context_object_name = 'category_list'
    def get_queryset(self):
        category_list = Category.objects.filter(sort__gt = 0)
        #goods_list = Goods.objects.all()

        return category_list





