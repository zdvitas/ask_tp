# -*- coding: utf-8 -*-
# coding: utf-8
#from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from ask.models import Questions
from ask.models import Answer
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
import datetime
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin
from ask.forms import add_quest_form
import json

def valid_login(data):
    response = {}
    response['status'] = 'ok'
    response['login_err'] = 'ok'
    response['pass_err'] = 'ok'
    if(data['login'] == ''):
        response['status'] = 'bad'
        response['login_err'] = 'not'
    if(data['password'] == ''):
        response['status'] = 'bad'
        response['pass_err'] = 'not'
    return response


def valid_reg(data):
    response = {}
    response['status'] = 'ok'
    response['login_err'] = 'ok'
    response['pass_err'] = 'ok'
    response['email_err'] = 'ok'
    if(data['login'] == ''):
        response['status'] = 'bad'
        response['login_err'] = 'not'
    if(data['password'] == ''):
        response['status'] = 'bad'
        response['pass_err'] = 'not'
    if(data['email'] == ''):
        response['status'] = 'bad'
        response['email_err'] = 'not'
    return response

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



def get_ajax_add_quest(request):
    form = add_quest_form(request.POST)
    response = {}

    if form.form_valid():
        response['result'] = 'ok'
        title = form.data['tittle']
        body = form.data['body']
        b2 = Questions(title=title, body=body, pub_date=datetime.datetime.now(), user=User(1))
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



class QuestList(ListView, FormMixin):

    model = Questions
    template_name = "questions_list.html"
    paginate_by = 10

    form_class = add_quest_form
    context_object_name = "quests"


    def get_context_data(self, **kwargs):
        context = super(QuestList, self).get_context_data(**kwargs)
        p = Paginator(object, 20)
        form_class = self.get_form_class()

        context['form'] = self.get_form(form_class)
        return context


class QuestDetailView(DetailView):
    model = Questions
    context_object_name = "quest"

    def get_context_data(self, **kwargs):

        context = super(QuestDetailView, self).get_context_data(**kwargs)
        # Получаем объект нашего вопроса, для загрузки ответов
        object = super(QuestDetailView, self).get_object()

        context['answers'] = Answer.objects.filter(quest=object).order_by('-pub_date')

        return context


