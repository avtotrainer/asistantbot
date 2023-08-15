import telebot
import requests

bot=telebot.TeleBot('6378752240:AAG_zouERwnCeXqIF-W5kcIktggpD17a63k')

wellcome_message = '''
 მოგესალმები {message.from_user.first_name} {message.from_user.last_name}!
 მე ვარ ბოტი და შევეცდები დაგეხმაროთ!
'''

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, wellcome_message.format(message=message))

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'დაგეხმარებით მეგობრებო!')


@bot.message_handler(commands=['cv'])
def show_html_page(message):
    github_html_url = 'https://github.com/avtotrainer/cv/blob/main/index.html'  # Замените на URL вашей HTML-страницы
    response = requests.get(github_html_url)
    
    if response.status_code == 200:
        html_content = response.text
        bot.send_message(message.chat.id, html_content, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, 'Не удалось загрузить HTML-страницу.')


bot.infinity_polling()
