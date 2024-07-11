from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import urllib

from django.views.generic import TemplateView

from .forms import LoginUserForm, RegisterUserForm


# Create your views here.
# def login_user(request, return_url=None):
#     '''
#     :param return_url: url-encoded страница, на которую следует перейти после входа в аккаунт.
#     '''
#     form = LoginUserForm()
#     data = {
#         'form': form
#     }
#
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             user = authenticate(**form.cleaned_data)
#             success = user is not None
#             data.update({'success': success})
#             if success and user.is_active:
#                 login(request, user)
#                 if return_url:
#                     return redirect(urllib.parse.unquote(return_url))
#                 return redirect('index')
#
#     return render(request, 'users/login.html', context=data)

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            cd = form.cleaned_data
            user.set_password(cd['password'])
            user.save()
            return redirect(reverse('register_success'))
        else:
            print('form is not valid')
    else:
        form = RegisterUserForm()
    data = {
        'form': form
    }
    return render(request, 'users/register.html', context=data)

class RegisterSuccessView(TemplateView):
    template_name = 'users/register_success.html'

class LoginUser(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginUserForm

    def get_default_redirect_url(self):
        return_url = self.kwargs.get('return_url', None)
        if return_url:
            clear_url = urllib.parse.unquote(return_url)
            return clear_url
        return reverse('index')


def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')
