__author__ = 'zdvitas'
from ask.views import valid_login
from django.contrib import auth
from django.http import HttpResponse
from ask.models import Questions
import datetime
from django.contrib.auth.models import User
from ask.forms import add_quest_form
import json

def get_ajax_logout(request):
    auth.logout(request)
    return HttpResponse('Ok')

def get_ajax_add_quest(request):
    form = add_quest_form(request.POST)
    response = {}

    if form.form_valid():
        response['result'] = 'ok'
        title = form.data['tittle']
        body = form.data['body']
        b2 = Questions(title=title, body=body, pub_date=datetime.datetime.now(), user=User(1), raiting=0)
        b2.save()
    else:
        response['result'] = 'bad'
        response['errors'] = form.error_list
    return HttpResponse(json.dumps(response))


def get_ajax_login(request):
    ans = {}
    req = {}
    req['login'] = request.POST['login']
    req['password'] = request.POST['password']
    ans = valid_login(req)
    if(ans['status'] == 'ok'):
        user = auth.authenticate(username=req['login'], password=req['password'])
        if user is not None and user.is_active:
            auth.login(request, user)
            ans['username'] = user.username
        else:
            ans['status'] = 'fail'

    return HttpResponse(json.dumps(ans))

def get_ajax_reg(request):
    ans = {}
    req = {}
    req['login'] = request.POST['login']
    req['password'] = request.POST['password']
    req['email'] = request.POST['email']
    ans = valid_login(req)
    if(ans['status'] == 'ok'):
        user = User.objects.create_user(req['login'], req['email'], req['password'])
        user.save()
        ans['username'] = user.username


    return HttpResponse(json.dumps(ans))
