# Веб-приложение для управления базой данных бонусных карт

![Django-app workflow](https://github.com/iricshkin/bonus_cards_project/actions/workflows/app-testing.yml/badge.svg)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)

## Функционал приложения

    1. список карт с полями: серия, номер, дата выпуска, дата окончания активности, статус
    2. поиск по этим же полям
    3. просмотр профиля карты с историей покупок по ней
    4. активация/деактивация карты
    5. удаление карты

Реализован генератор карт, с указанием серии и количества генерируемых карт, а также "срок окончания активности" со значениями "1 год", "6 месяцев" "1 месяц". После истечения срока активности карты, у карты проставляется статус "просрочена".

## Установка

Склонируйте репозиторий.

Находясь в папке с кодом создайте виртуальное окружение

`python -m venv venv`,

активируйте его:

Windows: `source venv\scripts\activate`;

Linux/Mac: `source venv/bin/activate`,

установите зависимости

`python -m pip install -r requirements.txt`.

Для запуска сервера разработки, находясь в директории проекта выполните команды:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Об авторе

Ирина Фок [iricshkin](https://github.com/iricshkin/)
