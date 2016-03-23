from django import forms
from qa.models import Question


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    author = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    def save(title, text):
        q = Question.objects.create(
            self.title = title,
            self.text = text,
            self.rating = 10,
            self.author = 1 )
        q.save()
        return q.get('id')
