from django import forms

class add_quest_form(forms.Form):
    tittle = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)

class add_answer_form(forms.Form):
    tittle = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
