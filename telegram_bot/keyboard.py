from telebot import types

def manu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    add_admin = types.KeyboardButton(text="ariza yuborish")
    describe = types.KeyboardButton(text='shikoyatt yubooriish')
    keyboard.add(add_admin)
    keyboard.add(describe)
    return keyboard
def ariza_bolimi():

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ish_sorash = types.KeyboardButton(text="Ish sorash")
    boshqa = types.KeyboardButton(text="Boshqa")
    ortga = types.KeyboardButton(text="Ortga")
    keyboard.add(ish_sorash)
    keyboard.add(boshqa)
    keyboard.add(ortga)
    return keyboard

def shikoya_bolimi():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot = types.KeyboardButton(text="Botdan shkoyat")
    wep = types.KeyboardButton(text="Wepdan shikoyat")
    boshqa = types.KeyboardButton(text="Boshqa")
    ortga = types.KeyboardButton(text="Ortga")
    keyboard.add(bot)
    keyboard.add(wep)
    keyboard.add(boshqa)
    keyboard.add(ortga)
    return keyboard
def admin_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    shikoyat_viwe = types.KeyboardButton(text="shikoyatlarni korish")
    arizlarni_viwe= types.KeyboardButton(text="arizlarni korish")
    add_admin = types.KeyboardButton(text="admin qoshish")
    keyboard.add(shikoyat_viwe)
    keyboard.add(arizlarni_viwe)
    keyboard.add(add_admin)
    return keyboard
