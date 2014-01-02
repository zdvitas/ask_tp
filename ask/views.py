# -*- coding: utf-8 -*-
# coding: utf-8
from django.shortcuts import render


from ask.models import Questions
from ask.models import Answer
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin
from ask.forms import add_quest_form



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




def user_info(request, id):
    context = {}
    user = User.objects.filter(id=id).get()
    context['cur_user'] = user
    context['questions'] = Questions.objects.filter(user=user).all()[0:20]
    context['answers'] = Answer.objects.filter(user=user).all()[0:20]
    return render(request, 'ask/user_tpl.html', context)



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
        context['state'] = 1;
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


