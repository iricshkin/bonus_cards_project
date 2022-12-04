from django.contrib import admin

from cards.models import BonusCard, Purchase


@admin.register(Purchase)
class PurcaseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'bonus_card',
        'price',
        'data_of_purchase',
    )
    list_filter = ('name',)


@admin.register(BonusCard)
class BonusCardAdmin(admin.ModelAdmin):
    date_hierarchy = 'last_used'
    list_display = (
        'id',
        'series',
        'number',
        'release_date',
        'expiry_date',
        'balance',
        'status',
    )
    list_filter = ('number',)
    search_fields = (
        'series',
        'number',
    )
