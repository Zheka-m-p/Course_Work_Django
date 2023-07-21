from django.urls import path  # импортируем путь, чтобы общараться можно было
from mailing_app.views import hello, ClientListView, ClientCreateView, \
    ClientUpdateView, ClientDeleteView, MessageListView, MessageCreateView, \
    MessageUpdateView, MessageDeleteView, SettingsListView, SettingsCreateView, \
    SettingsUpdateView, SettingsDeleteView, ClientDetailView, MessageDetailView, \
    SettingsDetailView, AttemptMailingListView, AttemptMailingDeleteView, \
    AttemptMailingDetailView, clear_db_attempt_mails  # импортируем нашу функцию-контролер
from mailing_app.apps import MailingAppConfig  # импортируем класс, в котором есть имя нашего приложения(само создано было)


app_name = MailingAppConfig.name  # задаем имя переменной для приложения

urlpatterns = [
    path('', hello),
    path('client_list/',  ClientListView.as_view(), name='client_list'),
    path('create_client/',  ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/',  ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/',  ClientDeleteView.as_view(), name='delete_client'),
    path('detail_client/<int:pk>/',  ClientDetailView.as_view(), name='detail_client'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('update_message/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),
    path('detail_message/<int:pk>/', MessageDetailView.as_view(), name='detail_message'),

    path('settings_list/', SettingsListView.as_view(), name='settings_list'),
    path('create_settings/', SettingsCreateView.as_view(), name='create_settings'),
    path('update_settings/<int:pk>/', SettingsUpdateView.as_view(), name='update_settings'),
    path('delete_settings/<int:pk>/', SettingsDeleteView.as_view(), name='delete_settings'),
    path('detail_settings/<int:pk>/', SettingsDetailView.as_view(), name='detail_settings'),

    path('attempt_mails_list/', AttemptMailingListView.as_view(), name='attempt_mails_list'),
    path('delete_attempt_mails/<int:pk>/', AttemptMailingDeleteView.as_view(), name='delete_attempt_mails'),
    path('detail_attempt_mails/<int:pk>/', AttemptMailingDetailView.as_view(), name='detail_attempt_mails'),

    path('clear_db_attempt_mails/', clear_db_attempt_mails, name='clear_db_attempt_mails')

]