from django import forms

from .choices import CARD_STATUS, DURATION, SERIES
from .models import BonusCard


class DateInput(forms.DateInput):
    input_type = 'date'


class CardForm(forms.ModelForm):
    """Форма для создания карт."""
    series = forms.CharField(
        label='Серия',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'XXXX'})
    )
    number = forms.IntegerField(
        label='Номер карты',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '12345678'})
    )
    status = forms.CharField(
        label='Статус карты',
        widget=forms.Select(choices=CARD_STATUS)
    )
    expiry_date = forms.DateTimeField(
        label='Дата окончания',
        widget=DateInput
    )
    balance = forms.DecimalField(
        label='Баланс',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Максимум цифр: 9'})
    )

    class Meta(object):
        model = BonusCard
        widgets = {'expiry_date': DateInput()}
        fields = (
            'series',
            'number',
            'expiry_date',
            'balance',
            'status'
        )


class CardGenerateForm(forms.Form):
    """Форма генерации карт"""

    series = forms.CharField(
        label='Серия',
        widget=forms.Select(choices=SERIES)
    )
    duration = forms.ChoiceField(
        choices=DURATION,
        label='Срок окончания активности'
    )
    quantity = forms.IntegerField(
        label='Количество',
        min_value=1
    )


class CardSearchForm(forms.Form):
    """Форма поиска."""

    search = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search'})
    )
