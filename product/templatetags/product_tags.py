from django import template

register = template.Library()

@register.inclusion_tag('product/tags/goods_info.html')
def load_goods_info(goods):

    return {

        'goods':goods
    }
