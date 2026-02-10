import threading
import telebot
from django.conf import settings
from .keyboard import manu, ariza_bolimi,shikoya_bolimi

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
        bot.send_message(chat_id, "arizani turini kriting" , reply_markup=ariza_bolimi())
        bot.register_next_step_handler(message, ariza_malumto_olish)
        return

    if message.text == "shikoyatt yubooriish":
        bot.send_message(chat_id, "shikoyatni turini kriting",reply_markup=shikoya_bolimi())
        bot.register_next_step_handler(message, shikoyat_malumot_olish)
        return

    else:
        send_welcome(message)
        return

info_ariza={}
info_shikoyat = {}
def ariza_malumto_olish(message):
    chat_id = message.chat.id
    user = message.from_user
    global info_ariza
    info_ariza.update({
        "user": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "chat id": chat_id,
        "ariza turi": message.text,

    })

    if message.text == "Sotib olish":
        bot.send_message(chat_id, "Sotib olish\n"
                                  "iltimos nima kerak eklangini yozisng\n"
                                  "qoshimcha malumotlar bilan ")
        bot.register_next_step_handler(message, Ariza)
        return

    if message.text == "Ish sorash":
        bot.send_message(chat_id, "Ish sorash")
        bot.register_next_step_handler(message, Ariza)
        return

    if message.text == "Boshqa":
        bot.send_message(chat_id, "Boshqa")
        bot.register_next_step_handler(message, Ariza)
        return

    if  message.text == "Ortga":
        bot.send_message(chat_id, "tanlang", reply_markup=manu())
        bot.register_next_step_handler(message, next_menu)
        return

    else:
        next_menu(message)
        return

def Ariza(message):
    chat_id = message.chat.id
    global info_ariza
    info_ariza.update({"ariza malumoti": message.text})
    bot.send_message(chat_id, "Ariza qabul qilindi",reply_markup=ariza_bolimi())
    bot.register_next_step_handler(message, ariza_malumto_olish)
    print("Ariza\n",info_ariza,"\n")
#============================================================================================================================================================

def shikoyat_malumot_olish(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id, "Tanlang")
    global info_shikoyat
    info_shikoyat.update({
        "user": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "chat id": chat_id,
        "shikoyat turi": message.text,

    })
    if message.text == "Botdan shkoyat":
        bot.send_message(chat_id, "Botdan shikoyatni kiritng")
        bot.register_next_step_handler(message, shikoyat)
        return
    if message.text == "Wepdan shikoyat":
        bot.send_message(chat_id, "Wepdan shikoyatni kiriting")
        bot.register_next_step_handler(message, shikoyat)
        return
    if message.text == "Boshqa shikoyat":
        bot.send_message(chat_id, "Boshqa shikoyatni kiriting")
        bot.register_next_step_handler(message, shikoyat)
        return
    if message.text == "Ortga":
        bot.send_message(chat_id, "tanlang", reply_markup=manu())
        bot.register_next_step_handler(message, next_menu)
        return

def shikoyat(message):
    chat_id = message.chat.id
    global info_shikoyat
    info_shikoyat.update({"shuikoyat malumoti": message.text})
    bot.send_message(chat_id, "shikoyat qabul qilindi",reply_markup=shikoya_bolimi())
    bot.register_next_step_handler(message, shikoyat_malumot_olish)
    print("shikoyat\n",info_shikoyat,"\n")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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