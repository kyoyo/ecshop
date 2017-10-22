from django.contrib import admin
from .models import Adv, Notice


# Register your models here.

class AdvAdmin(admin.ModelAdmin):
    list_display = ['title', 'order_value', 'image','status']
    fields = ('title', 'order_value','image','status')


admin.site.register(Adv, AdvAdmin)
admin.site.register(Notice)
