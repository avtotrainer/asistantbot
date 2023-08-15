import telebot

bot=telebot.TeleBot('6450641365:AAEJyLYrQJkq_HUgmftauH8uOwVpx7krHuo')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'ვაა, ბარო')

bot.polling(non_stop=True)