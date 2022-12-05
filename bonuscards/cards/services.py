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
