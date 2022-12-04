from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone


class BonusCard(models.Model):
    """Бонусная карта."""

    CARD_STATUS = (
        ('active', 'Активирована'),
        ('inactivated', 'Не активирована'),
        ('overdue', 'Просрочена')
    )

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'
        constraints = [
            models.UniqueConstraint(
                fields=['series', 'number'],
                name='unique_series_number',
            ),
        ]

    series = models.CharField(
        verbose_name='Серия',
        max_length=4,
        validators=[
            RegexValidator(r'^[-A-Z0]+$', 'Неверная серия карты!'),
        ],
    )
    number = models.PositiveIntegerField(
        verbose_name='Номер карты',
    )
    release_date = models.DateTimeField(
        verbose_name='Дата выпуска',
        default=datetime.now,
    )
    expiry_date = models.DateTimeField(
        verbose_name='Дата окончания',
    )
    last_used = models.DateTimeField(
        verbose_name='Последнее использование',
        auto_now=True,
    )
    balance = models.DecimalField(
        verbose_name='Баланс',
        decimal_places=2,
        max_digits=9,
    )
    status = models.CharField(
        verbose_name='Статус карты',
        max_length=40,
        choices=CARD_STATUS,
    )

    def clean(self, *args, **kwargs):
        if len(str(self.number)) == 8:
            return super().clean(*args, **kwargs)
        raise ValidationError('Номер карты состоит из 8 цифр!')

    def save(self, *args, **kwargs) -> None:
        self.full_clean()

        datetime_now = timezone.now()
        if datetime_now >= self.expiry_date:
            self.status = 'overdue'

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Бонусная карта {self.series} {self.number}'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'card_number': self.number})


class Purchase(models.Model):
    """Покупки."""

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    name = models.CharField(
        verbose_name='Название покупки',
        max_length=150,
    )
    bonus_card = models.ForeignKey(
        BonusCard,
        verbose_name='Бонусная карта',
        on_delete=models.CASCADE,
        related_name='purchase',
    )
    price = models.DecimalField(
        verbose_name='Цена покупки',
        decimal_places=2,
        max_digits=7,
    )
    data_of_purchase = models.DateTimeField(
        verbose_name='Дата покупки',
        auto_now_add=True,
    )

    def clean(self, *args, **kwargs):
        card_status = self.bonus_card.status

        if card_status == 'active':
            return super().clean(*args, **kwargs)
        else:
            if card_status == 'inactivated':
                raise ValidationError('Ваша карта не активирована!')
            raise ValidationError('Ваша карта просрочена!')

    def __str__(self) -> str:
        price = f'{self.price:,}'.replace(',', ' ')
        return f'{self.name} {price}$'
