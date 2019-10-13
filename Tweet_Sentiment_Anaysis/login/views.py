from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
message=''
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):

    username = request.POST.get('username', '')
    username1=username.lower()
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username1,password=password)
    if user is not None:
        auth.login(request, user)
        if 'login' not in request.session:
            request.session['login'] = username

        c = {}
        c.update(csrf(request))
        return HttpResponseRedirect('/analysis/index')
    else:
        c = {}
        message = "invalid Username or Password"
        c['er'] = message
        c.update(csrf(request))
        return render_to_response('login.html', c)

@login_required(login_url='/login/')

def logout(request):
    c = {}
    del request.session['login']
    c.update(csrf(request))
    auth.logout(request)
    return render_to_response('login.html', c)
