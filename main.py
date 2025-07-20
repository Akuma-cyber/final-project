import telebot,os,random
import requests
from bs4 import BeautifulSoup
#import pandas as pd
from pars import pars
bot = telebot.TeleBot("7314930912:AAGC-D_tmIfJkwggIi_GXE2y-klwp5tBWbI")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Приветствую тебя!Я бот про очень серьёзную промблему глобальное потепление.Задавай любой вопрос и я на него отвечу")


@bot.message_handler(commands=['info'])
def send_info(message):
    title,text = pars()
    bot.reply_to(message,f"{title}\n{text}" )


@bot.message_handler(commands=['facts'])
def send_info(message):
    title,text = banana()
    bot.reply_to(message,f"{title}\n{text}" )



bot.polling()
