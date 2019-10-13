from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def register(request):

    c = {}
    c.update(csrf(request))
    return render_to_response('signup.html', c)

def auth_view(request):
    c = {}
    username = request.POST.get('username', '')
    username1=username.lower()
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    repassword = request.POST.get('repassword', '')
    try :
        user = User.objects.get(username=username1)
        message = "Username is Taken Choose Diffrent username"
        c['er'] = message
        c.update(csrf(request))
        return render_to_response('signup.html', c)

    except User.DoesNotExist:
        try:
            validate_email(email)
        except ValidationError as e:
            message = "Please Enter Valid Email"
            c['er'] = message
            c.update(csrf(request))
            return render_to_response('signup.html', c)
        else:
            if password != repassword:
                message = "Password and ReEnter Password must be same"
                c['er'] = message
                c.update(csrf(request))
                return render_to_response('signup.html', c)
            else:
                user = User.objects.create_user(username=username1, email=email, password=password)
                user.save()
                message = "   You are sign Up!!!"
                c['er'] = message
                c.update(csrf(request))
                return render_to_response('login.html', c)




