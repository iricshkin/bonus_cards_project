import random

from .models import BonusCard


def _search_results(search: str) -> list:
    """Выполняет поиск по указанному запросу."""

    res = []
    cards = BonusCard.objects.all()

    for card in cards:

        if search in str(card.series) and cards not in res:
            res.append(card)

        elif search in str(card.number) and cards not in res:
            res.append(card)

        elif search in str(card.release_date) and cards not in res:
            res.append(card)

        elif search in str(card.expiry_date) and cards not in res:
            res.append(card)

        elif search in str(card.status) and cards not in res:
            res.append(card)

    return res


def _generate_card_numbers(n) -> list:
    """Генерирует указанное количество номеров бонусных карты"""
    MIN_NUMBER = 10000000
    MAX_NUMBER = 99999999

    generated_list = []
    created = 0

    while created < int(n):

        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in generated_list:
            generated_list.append(number)
            created += 1

    return generated_list
