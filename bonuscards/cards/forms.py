from django import forms

SERIES = [
    ('AAAA', 'AAAA'),
    ('BBBB', 'BBBB'),
    ('ABCD', 'ABCD')
]

DURATION = (
    (1, '1 месяц'),
    (6, '6 месяцев'),
    (12, '1 год'),
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
