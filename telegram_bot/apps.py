from django.apps import AppConfig

class TelegramBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram_bot'

    def ready(self):
        import os
        if os.environ.get('RUN_MAIN') == 'true':
            # ✅ To'g'ri import: 'telegram_bot.bot' deb ko'rsatish kerak
            from . import bot
            bot.start_bot()