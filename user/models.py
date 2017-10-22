from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class UserProfile(AbstractUser):

    SEX = (
        ('0','保密'),
        ('1','男'),
        ('2','女'),
    )

    USER_STATUS = (
        ('0','停用'),
        ('1','启用'),
    )

    USER_RANK = (
        ('0','普通会员'),
        ('1','铜牌会员'),
        ('2','银牌会员'),
        ('3','金牌会员'),
    )

    nickname = models.CharField('昵称',max_length=50,blank=True)
    realname = models.CharField('姓名',max_length=50,blank=True)
    sex = models.CharField('性别',max_length=1,blank=True,null=True,choices=SEX)
    birth = models.DateField('生日',blank=True,null=True)
    head_img = models.ImageField(upload_to='user/%Y/%m', verbose_name='头像', blank=True, default='', max_length=500)
    mobile = models.CharField(verbose_name='联系方式', max_length=11,blank=True)
    integral = models.IntegerField(default=0, verbose_name='积分')
    balance = models.DecimalField(decimal_places=2, max_digits=8,default=0.0, verbose_name='余额')
    user_status = models.CharField('用户状态',max_length=1,default= '1', choices=USER_STATUS)
    user_rank = models.CharField('用户级别',max_length=1,blank=True,default= '0',choices=USER_RANK)
    remark = models.TextField(verbose_name='备注',blank=True )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name ='用户'
        verbose_name_plural = verbose_name

class UserAddress(models.Model):
    user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name='用户')
    address = models.CharField(max_length=500, verbose_name='收件地址')
    name = models.CharField(max_length=20, verbose_name='收件人')
    mobile = models.CharField(max_length=30, verbose_name='手机号')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name
