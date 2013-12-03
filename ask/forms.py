from django import forms

class add_quest_form(forms.Form):
    tittle = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
    error_list = {}

    def form_valid(self):
        self.error_list['tittle'] = 'ok'
        self.error_list['body'] = 'ok'
        if(self.data['tittle'] == ''):
            self.error_list['tittle'] = 'err'
            return 0

        if(self.data['body'] == ''):
            self.error_list['body'] = 'err'
            return 0
        return 1



class add_answer_form(forms.Form):
    tittle = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)

