from cards.models import BonusCard
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView

from .forms import CardSearchForm
from .services import _search_results


def index(request):
    """Главная страница."""

    if request.GET.get('search'):
        cards = _search_results(request.GET.get('search'))

    else:
        cards = BonusCard.objects.all()
        paginator = Paginator(cards, 5)
        page = request.GET.get('page')
        cards = paginator.get_page(page)

    form = CardSearchForm()

    context = {
        'cards': cards,
        'form': form,
    }

    return render(request, 'cards/index.html', context=context)


class CardDetailView(DetailView):
    """Страница бонусной карты."""
    queryset = BonusCard.objects.all()
    context_object_name = 'card'
    template_name = 'cards/profile.html'


def activate(request, pk):
    """Активация карты."""
    card = BonusCard.objects.get(pk=pk)
    card.status = 'active'
    card.save()

    return redirect('profile', card.pk)


def deactivate(request, pk):
    """Деактивация карты."""
    card = BonusCard.objects.get(pk=pk)
    card.status = 'inactivated'
    card.save()

    return redirect('profile', card.pk)


def delete(reques, pk):
    """Удаление карты."""
    card = BonusCard.objects.get(pk=pk)
    card.delete()

    return redirect('home')
