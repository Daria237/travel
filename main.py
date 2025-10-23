import random
import telebot
from typing import Dict, List, Tuple

BOT_TOKEN = '8266335546:AAGi3S6qoOtIQ07xMV-az8x053zl1uNwzr8'

bot = telebot.TeleBot(BOT_TOKEN)

# Словари для хранения состояний пользователей
user_states = {}