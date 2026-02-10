import threading
import telebot
from telegram import Update
from django.conf import settings
from clients.models import Client
from .keyboard import manu, ariza_bolimi

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "tanlang",reply_markup=manu())
    bot.register_next_step_handler(message, next_menu)
    # user = message.from_user
    # client, created = Client.objects.get_or_create(
    #     telegram_id=user.id,
    #     defaults={
    #         "name": user.first_name or "Noma'lum",
    #         "phone": "test"  # Telefon keyinchalik so'raladi
    #     }
    # )
    # f"🆔 ID: {user.id}\n"
    # f"👤 Ism: {user.first_name}\n"
    # f"👥 Familiya: {user.last_name}\n"
    # f"🔗 Username: @{user.username}\n"
    # f"🌐 Til: {user.language_code}\n"
    # f"🤖 Botmi: {user.is_bot}"
def next_menu(message):
    chat_id = message.chat.id
    if message.text == "ariza yuborish":
        bot.send_message(chat_id, "arizani kriting" , reply_markup=ariza_bolimi())
        bot.register_next_step_handler(message, ariza_malumto_olish)
        return
    if message.text == "shikoyatt yubooriish":
        bot.send_message(chat_id, "shikoyatni kriting")
        bot.register_next_step_handler(message, next_menu)
        return
    else:
        send_welcome(message)
        return
def uzatuvchi(message):
    chat_id = message.chat.id
    info = {
        "user": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "email": message.from_user.email,

    }
def ariza_malumto_olish(message):
    chat_id = message.chat.id
    user = message.from_user

    if message.text == "Sotib olish":
        bot.send_message(chat_id, "Sotib olish")
        bot.register_next_step_handler(message, ariza_malumto_olish)
        return

    if message.text == "Ish sorash":
        bot.send_message(chat_id, "Ish sorash")
        bot.register_next_step_handler(message, ariza_malumto_olish)
        return

    if message.text == "Boshqa":
        bot.send_message(chat_id, "Boshqa")
        bot.register_next_step_handler(message, ariza_malumto_olish)
        return

    if  message.text == "Ortga":
        bot.send_message(chat_id, "tanlang", reply_markup=manu())
        bot.register_next_step_handler(message, next_menu)
        return

    else:
        ariza_malumto_olish(message)
        return

def run_bot():
    """Botni polling rejimida ishga tushirish"""
    print("🤖 pyTelegramBotAPI bot ishga tushdi...")
    bot.infinity_polling()  # Doimiy ishlash

def start_bot():
    """Botni alohida thread da ishga tushirish (Django block qilmasligi uchun)"""
    import os
    if os.environ.get('RUN_MAIN') == 'true':  # Faqat bir marta ishlasin
        thread = threading.Thread(target=run_bot, daemon=True)
        thread.start()