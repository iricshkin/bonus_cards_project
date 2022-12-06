from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import CardForm, CardGenerateForm, CardSearchForm
from .models import BonusCard
from .services import _generate_card_numbers, _search_results


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
    """Страница профиля бонусной карты."""
    queryset = BonusCard.objects.all()
    context_object_name = 'card'
    template_name = 'cards/profile.html'


class CardCreateView(SuccessMessageMixin, CreateView):
    """Создание бонусной карты"""
    model = BonusCard
    form_class = CardForm
    template_name = 'cards/create.html'
    success_url = reverse_lazy('home')


def activate(request, pk):
    """Активация бонусной карты."""
    card = BonusCard.objects.get(pk=pk)
    card.status = 'active'
    card.save()

    return redirect('profile', card.pk)


def deactivate(request, pk):
    """Деактивация бонусной карты."""
    card = BonusCard.objects.get(pk=pk)
    card.status = 'inactivated'
    card.save()

    return redirect('profile', card.pk)


def delete(reques, pk):
    """Удаление бонусной карты."""
    card = BonusCard.objects.get(pk=pk)
    card.delete()

    return redirect('home')


def generate(request):
    """Генерирует бонусные карты."""

    if request.method == 'POST':

        form = CardGenerateForm(request.POST)
        if form.is_valid():
            series = form.cleaned_data['series']
            quantity = int(form.cleaned_data['quantity'])
            duration = int(form.cleaned_data['duration'])

            generated_cards_number = _generate_card_numbers(quantity)

            release_date = datetime.now()
            expiry_date = release_date + relativedelta(months=duration)

            context = {
                'series': series,
                'numbers': generated_cards_number,
                'release_date': release_date,
                'expiry_date': expiry_date,
                'status': 'Не активирована'
            }
            return render(
                request,
                'cards/generate_result.html',
                context=context
            )

    form = CardGenerateForm()
    context = {
        'form': form,
    }

    return render(request, 'cards/generate.html', context=context)
