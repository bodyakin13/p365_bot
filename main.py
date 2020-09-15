import telebot
import random
import config

bot = telebot.TeleBot(config.token)

start = open(file='text/start.txt', mode='r', encoding='utf-8').read()

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, start)

@bot.message_handler(commands=['p365'])
def p365(message):
    num = random.randrange(1, 23750)
    bot.send_message(message.chat.id, 'http://porno365.work/movie/' + str(num))

bot.polling(none_stop = True)  


