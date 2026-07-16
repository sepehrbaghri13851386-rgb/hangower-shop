from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'has_reply')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')

    # پیام اصلی کاربر رو قفل می‌کنیم تا ادمین نتونه دستکاریش کنه
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at', 'replied_at')
    fields = ('name', 'email', 'subject', 'message', 'created_at', 'reply', 'replied_at')

    def has_reply(self, obj):
        return bool(obj.reply)
    has_reply.boolean = True
    has_reply.short_description = "پاسخ داده شده؟"