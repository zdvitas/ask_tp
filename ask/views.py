#from django.shortcuts import render
from django.http import HttpResponse
from ask.models import Questions
from django.views.generic import ListView ,DetailView
import datetime
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin

from django.http import HttpResponseRedirect
from django.shortcuts import render
from ask import forms


class QuestList(ListView, FormMixin):

    model = Questions
    template_name = "questions_list.html"
    paginate_by = 10
    form_class = forms.add_quest_form
    context_object_name = "quests"

    def get_context_data(self, **kwargs):
        context = super(QuestList, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
        #self.object = self.get_object()
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                title = form.cleaned_data['tittle']
                body = form.cleaned_data['body']
                b2 = Questions(title=title, body=body, pub_date=datetime.datetime.now(), user=User(1))
                b2.save()
                return HttpResponse('Thanks!')
            return form.errors


class QuestDetailView(DetailView):
    model = Questions


#def contact(request):
#    if request.method == 'POST':
#        form = forms.add_quest_form(request.POST)
#        if form.is_valid():
#            title = form.cleaned_data['tittle']
#            body = form.cleaned_data['body']
#            b2 = Questions(title=title, body=body, pub_date=datetime.datetime.now() ,user=User(1))
#            b2.save()
#            return HttpResponse('Thanks!')
#        return HttpResponse('FUCK!')
#    else:
#        form = forms.add_quest_form()
#    p = QuestList.objects.value()
#    return render(request, 'ask/questions_list.html', {
#        "quests": p,
#        'form': form,
#    })
