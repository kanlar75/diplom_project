from django.contrib import admin

from ads.models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Объявления - отображение в админ-панели Jango.
    Фильтрует по ФИ автора и названию товара.
    Поиск в названии товара и его описании.
    """
    list_display = ('pk', 'user', 'title', 'price', 'created_at')
    list_filter = ('user', 'title',)
    search_fields = ('title', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Комментарии - отображение в админ-панели Jango.
    Фильтрует по ФИ автора.
    """
    list_display = ('pk', 'ad', 'user', 'text', 'created_at')
    list_filter = ('user',)
