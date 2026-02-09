from django.db import models
from django.contrib.auth.models import User
from clients.models import Client

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'Yangi'),
        ('contacted', 'Aloqada'),
        ('converted', 'Sotildi'),
        ('rejected', 'Rad etildi'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Mijoz")
    service = models.CharField("Xizmat", max_length=100)
    description = models.TextField("Tavsif", blank=True)
    status = models.CharField("Holat", max_length=20, choices=STATUS_CHOICES, default='new')
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Mas'ul xodim"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name} — {self.service}"