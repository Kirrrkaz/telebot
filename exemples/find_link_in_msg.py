import telebot
import config
from urllib.parse import parse_qsl, urljoin, urlparse
import urllib.parse as urlparse

bot = telebot.TeleBot(config.API_TOKEN)



@bot.message_handler(commands=['start', 'help'])
def handle_message(message):
    sent = bot.send_message(message.chat.id, "Введите ссылку, а я это проверю :)")
    bot.register_next_step_handler(sent, save_link)
    

def save_link(message):
    my_link = message.text
    
    if urlparse.urlparse(message.text).scheme:
        
        bot.send_message(message.chat.id, "Да, это ссылка")
    else:
        bot.send_message(message.chat.id, "Это не ссылка")
