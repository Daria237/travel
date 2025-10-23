import random
import telebot
from typing import Dict, List, Tuple

BOT_TOKEN = '8266335546:AAGi3S6qoOtIQ07xMV-az8x053zl1uNwzr8'

bot = telebot.TeleBot(BOT_TOKEN)

# Словари для хранения состояний пользователей
user_states = {}
class UrbanExplorer:
    def __init__(self):
        self.adventure_data = self._load_adventure_data()
        self.additional_tasks = self._load_additional_tasks()
        self.adventure_types = {
            "1": "photographer",
            "2": "historian", 
            "3": "foodie",
            "4": "fun"
        }
        self.districts = {
            "1": "nizhegorodsky",
            "2": "sovetsky",
            "3": "prioksky"
        }
        self.district_names = {
            "nizhegorodsky": "Нижегородский",
            "sovetsky": "Советский",
            "prioksky": "Приокский"
        }
        self.type_names = {
            "photographer": "Фотограф-исследователь 📸",
            "historian": "Историк-детектив 🕵️",
            "foodie": "Гастроном-путешественник 🍜",
            "fun": "Фанат атмосферных развлечений 🎭"
        }