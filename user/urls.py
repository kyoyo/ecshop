from django.conf.urls import url,include
from .views import LoginView,LogoutView,RegisterView,UserProfileView

urlpatterns = [
    url('^login/$',LoginView.as_view(),name='login'),
    url('^register/$',RegisterView.as_view(),name='register'),
    url('^logout/$',LogoutView.as_view(),name='logout'),
    url('^userprofile/$',UserProfileView.as_view(),name='userprofile'),


]
