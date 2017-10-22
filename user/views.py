from django.shortcuts import render
from django.views.generic import FormView,RedirectView,TemplateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm,RegisterForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils.http import is_safe_url
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'user/register.html'

    def form_valid(self, form):
        pass
        # user = form.save(False)
        # user.save(True)
        # url = reverse('accounts:login')
        # return HttpResponseRedirect(url)


class LogoutView(RedirectView):
    url = '/'
    def get(self, request, *args, **kwargs):
        logout(request)

        return super(LogoutView,self).get(request,*args,**kwargs)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'
    redirect_field_name = REDIRECT_FIELD_NAME



    def get(self, request, *args, **kwargs):

        return super(LoginView,self).get(request,*args, **kwargs)


    def post(self, request, *args, **kwargs):
        return super(LoginView,self).post(request, *args, **kwargs)


    def form_valid(self,form):

        form = AuthenticationForm(request= self.request,data=self.request.POST)

        if form.is_valid():
            login(self.request,form.get_user())

            return super(LoginView,self).form_valid(form)
        else:
            return self.render_to_response(
                {
                    'form':form
                }
            )

    def get_context_data(self, **kwargs):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to is None:
            redirect_to = '/'
        kwargs['redirect_to'] = redirect_to
        return super(LoginView,self).get_context_data(**kwargs)

    def get_success_url(self):
        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to

class UserProfileView(TemplateView):
    template_name = 'user/index.html'