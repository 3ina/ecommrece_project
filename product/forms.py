from django import forms


class Contact(forms.Form):
    firstname = forms.CharField(max_length=255,widget=forms.TextInput(attrs = {
            'class' : "form-control",
    }),required=True)
    lastname = forms.CharField(max_length=255,widget=forms.TextInput(attrs = {
            'class' : "form-control",
    }),required=True)
    email = forms.EmailField(max_length=255,widget=forms.TextInput(attrs = {
            'class' : "form-control",
    }),required=True)
    subject = forms.CharField(max_length=255,widget=forms.TextInput(attrs = {
            'class' : "form-control",
    }),required=True)
    message = forms.CharField(widget=forms.Textarea(attrs = {
            'class' : "form-control",
            'cols' : "30",
            'rows' : "7"
    }),required=True)