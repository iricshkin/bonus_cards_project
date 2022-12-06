from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/<int:pk>', views.CardDetailView.as_view(), name='profile'),
    path('add/', views.CardCreateView.as_view(), name='add'),
    path('generate/', views.generate, name='generate'),
    path('activate/<int:pk>', views.activate, name='activate'),
    path('deactivate/<int:pk>', views.deactivate, name='deactivate'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
