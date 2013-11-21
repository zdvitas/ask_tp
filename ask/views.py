#from django.shortcuts import render
from django.http import HttpResponse
from ask.models import Questions
from django.views.generic import ListView

from django.http import HttpResponseRedirect
from django.shortcuts import render
from ask import forms


class QuestList(ListView):
    model = Questions
    template_name = "question_list.html"
    paginate_by = 10

#def contact(request):
#    if request.method == 'POST':
#        form = forms.add_quest_form(request.POST)
#        if form.is_valid():
#            title = form.cleaned_data['tittle']
#            body = form.cleaned_data['body']
#            b2 = Questions(title=title, body=body)
#            b2.save()
#            return HttpResponse('Thanks!')
#        return  HttpResponse('FUCK!')
#    else:
#        form = forms.add_quest_form()
#    return render(request, 'main_tpl.html', {
#        'form': form,
#    })
