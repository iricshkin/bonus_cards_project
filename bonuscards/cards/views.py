from cards.models import BonusCard
from django.core.paginator import Paginator
from django.shortcuts import redirect, render


def index(request):
    """Главная страница."""
    cards = BonusCard.objects.all()
    paginator = Paginator(cards, 5)
    page = request.GET.get('page')
    cards = paginator.get_page(page)

    return render(request, 'cards/index.html', {'cards': cards})


def profile(request, card_number):
    """Страница бонусной карты."""
    card = BonusCard.objects.get(pk=card_number)
    balance = f'{card.balance:,}'.replace(',', ' ')
    context = {
        'card': card,
        'balance': balance,
    }

    return render(request, 'cards/profile.html', context=context)


def activate(request, card_number):
    """Активация карты."""
    card = BonusCard.objects.get(pk=card_number)
    card.status = 'active'
    card.save()

    return redirect('profile', card.pk)


def deactivate(request, card_number):
    """Деактивация карты."""
    card = BonusCard.objects.get(pk=card_number)
    card.status = 'inactivated'
    card.save()

    return redirect('profile', card.pk)


def delete(reques, card_number):
    """Удаление карты."""
    card = BonusCard.objects.get(pk=card_number)
    card.delete()

    return redirect('home')
