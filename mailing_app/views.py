from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from mailing_app.models import Client, Message, Settings, AttemptMailing


def hello(request):
    return render(request,
                  'mailing_app/base.html')  # процесс сбора всей информации, единое изображение(отображает страницу)


class ClientListView(ListView):
    model = Client
    # template_name = 'mailing/client/client_form.html'  добавить путь, чтобы было можно был в папки долбавлять



class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('mailing_app:client_list')


class ClientDetailView(DetailView):
    model = Client
    fields = '__all__'


class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('mailing_app:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('mailing_app:client_list')


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('mailing_app:message_list')


class MessageDetailView(DetailView):
    model = Message
    fields = '__all__'


class MessageUpdateView(UpdateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('mailing_app:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('mailing_app:message_list')


class SettingsListView(ListView):
    model = Settings


class SettingsCreateView(CreateView):
    model = Settings
    fields = '__all__'
    success_url = reverse_lazy('mailing_app:settings_list')


class SettingsDetailView(DetailView):
    model = Settings
    fields = '__all__'


class SettingsUpdateView(UpdateView):
    model = Settings
    fields = '__all__'
    success_url = reverse_lazy('mailing_app:settings_list')


class SettingsDeleteView(DeleteView):
    model = Settings
    fields = '__all__'
    success_url = reverse_lazy('mailing_app:settings_list')


class AttemptMailingListView(ListView):
    model = AttemptMailing


class AttemptMailingDetailView(DetailView):
    model = AttemptMailing
    fields = '__all__'



class AttemptMailingDeleteView(DeleteView):
    model = AttemptMailing
    fields = '__all__'
    success_url = reverse_lazy('mailing_app:attempt_mails_list')


def clear_db_attempt_mails(request):
    if request.method == 'POST':
        records = AttemptMailing.objects.all()
        records.delete()

        if True:
            return redirect('/attempt_mails_list/')

    return render(request, 'mailing_app/clear_db_attempt_mails.html')  #