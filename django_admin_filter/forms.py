from django import forms
from .models import Filter


class FilterForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        required=False,
        widget=forms.widgets.TextInput(
            attrs=dict(placeholder='optional')
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea(attrs=dict(
            rows=4,
            placeholder='optional'
        ))
    )

    class Meta:
        model = Filter
        fields = ['name', 'description']