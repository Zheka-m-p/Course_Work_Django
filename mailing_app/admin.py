from django.contrib import admin
from mailing_app.models import Client, Message, AttemptMailing, Settings


@admin.register(Client)  # создаем декоратор над класcом(чтобы как надо выводить)
class CaterogyAdmin(admin.ModelAdmin):
    list_display = ('email', 'fio', 'comment', 'id',)  # добавляем нужные нам колонки для отображения на сайте
    search_fields = ('email', 'fio',)  # добавляем поле поиска по данным колонкам
    list_filter = ('email', 'fio',)  # добавляем фильтрауцию по данной колонке, можем даже добавлять несколько фильтро


@admin.register(Message)  # создаем декоратор над класcом(чтобы как надо выводить)
class CaterogyAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)  # добавляем нужные нам колонки для отображения на сайте
    list_filter = ('title',)  # добавляем поле поиска по данным колонкам


@admin.register(Settings)  # создаем декоратор над класcом(чтобы как надо выводить)
class CaterogyAdmin(admin.ModelAdmin):
    list_display = ('time', 'period', 'status', 'message',)  # добавляем нужные нам колонки для отображения на сайте
    search_fields = ('period', 'status', 'message',)  # добавляем поле поиска по данным колонкам


@admin.register(AttemptMailing)  # создаем декоратор над класcом(чтобы как надо выводить)
class CaterogyAdmin(admin.ModelAdmin):
    list_display = ('last_attempt_date_time', 'status', 'server_response', 'settings_pk')  # добавляем нужные нам колонки для отображения на сайте
    search_fields = ('last_attempt_date_time', 'status', 'server_response',) # добавляем поле поиска по данным колонкам
