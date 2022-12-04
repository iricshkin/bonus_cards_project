from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/<int:card_number>', views.profile, name='profile'),
    path('activate/<int:card_number>', views.activate, name='activate'),
    path('deactivate/<int:card_number>', views.deactivate, name='deactivate'),
    path('delete/<int:card_number>', views.delete, name='delete'),
]
