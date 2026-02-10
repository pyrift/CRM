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
    sotib_olish = types.KeyboardButton(text="Sotib olish ")
    ish_sorash = types.KeyboardButton(text="Ish sorash")
    boshqa = types.KeyboardButton(text="Boshqa")
    ortga = types.KeyboardButton(text="Ortga")
    keyboard.add(sotib_olish)
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