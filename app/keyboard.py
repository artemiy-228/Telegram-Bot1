from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)
import json
import sqlite3


conn = sqlite3.connect('tg.db')
cur = conn.cursor()

with open('Sources.json', 'r', encoding='utf-8') as file:
    sources_data = json.load(file)


main_kb = [
    [KeyboardButton(text='О нас')],
    [KeyboardButton(text='Контакты')],
    [KeyboardButton(text='Подписаться на рассылку')],
    [KeyboardButton(text='Отписаться от рассылки')],
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder="Выберите пункт ниже")
sources_kb = []
for item in sources_data:
    button = InlineKeyboardButton(text=item['text'], url=item['url'])
    sources_kb.append([button])


socials = InlineKeyboardMarkup(inline_keyboard=sources_kb)

