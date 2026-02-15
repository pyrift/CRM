import telebot
from django.conf import settings
from .keyboard import manu, ariza_bolimi,shikoya_bolimi,admin_menu
import json
bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

def  get_information(message):
    chat_id = message.chat.id
    if message.text == "shikoyatlarni korish":
        with open("json_data/info_shikoyat.json", "r") as file:
            data = json.load(file)
        print(data)
    if message.text == "arizlarni korish":
        bot.send_message(chat_id, "test")
