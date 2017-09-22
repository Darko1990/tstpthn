import telebot

TOKEN = '438105784:AAHYiBA9LHkSiw3699IMj47dQ3LlOgR1oQE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Whats ur name?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, 'Hello, {name}!'.format(name=message.text))

bot.polling()