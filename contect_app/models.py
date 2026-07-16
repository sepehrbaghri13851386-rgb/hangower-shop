from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    reply = models.TextField(blank=True, null=True, verbose_name="پاسخ ادمین")
    replied_at = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ پاسخ")

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.reply and not self.replied_at:
            self.replied_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.subject}"
