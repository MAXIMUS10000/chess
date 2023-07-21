import  telebot

def  bot(x1,x2,y1,y2,isread):
    mes=''
    API_TOKEN = '6350182455:AAH4BfjzS9dnTPaIcbjQ6ZgUVF16RyvjnqI'

    bot = telebot.TeleBot(API_TOKEN)

    @bot.message_handler(func=lambda message: True)
    def echo_message(message):
        if isread:
            mes=message.text.split()

    return mes

    bot.infinity_polling()