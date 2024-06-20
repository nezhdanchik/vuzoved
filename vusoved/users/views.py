from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import urllib

from .forms import LoginUserForm


# Create your views here.
def login_user(request, return_url=None):
    '''
    :param return_url: url-encoded страница, на которую следует перейти после входа в аккаунт.
    '''
    form = LoginUserForm()
    data = {
        'form': form
    }

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():

            user = authenticate(**form.cleaned_data)
            success = user is not None
            data.update({'success': success})

            if success:
                login(request, user)
                if return_url:
                    return redirect(urllib.parse.unquote(return_url))
                return redirect('index')

    return render(request, 'users/login.html', context=data)


def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')

def tst(request, t=None):
    print(t)
    return redirect('/hello/')
