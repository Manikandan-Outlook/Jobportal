from django import forms


class UserInputForm(forms.Form):

    name = forms.CharField(widget=forms.Textarea, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    resumetitle = forms.CharField(widget=forms.Textarea, required=True)