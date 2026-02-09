from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['client', 'service', 'status', 'assigned_to', 'created_at']
    list_filter = ['status', 'assigned_to']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            # Agar foydalanuvchi superuser bo'lmasa, faqat o'ziga biriktirilganlarni ko'rsin
            return qs.filter(assigned_to=request.user)
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "assigned_to":
            # Faqat o'zini tanlasin (agar menejer bo'lsa)
            if not request.user.is_superuser:
                kwargs["queryset"] = type(request.user).objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)