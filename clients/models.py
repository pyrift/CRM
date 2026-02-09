from django.db import models

class Client(models.Model):
    name = models.CharField("Ism", max_length=100)
    phone = models.CharField("Telefon", max_length=20, unique=True)
    telegram_id = models.BigIntegerField("Telegram ID", null=True, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone}):"