from django import forms
from counter_widgets import CounterWidget

class AddToCartForm(forms.Form):
    size_choice = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Extra Large', 'Extra Large'),

    )

    size = forms.RadioSelect(choices=size_choice,attrs={
        "class":"d-inline-block mr-2",
        "style":"top:-2px; position: relative;",
    })

    quantity = forms.IntegerField(widget=CounterWidget(increment_text="+",decrement_text='-',increment_value=1,decrement_value=1,attrs={
        'class' : 'form-control text-center',
    }))