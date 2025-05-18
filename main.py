import telebot
from telebot import types

import sqlite3

TOKEN = "8082314121:AAFRRaTx66mItLu4kx-3BmlwzptMU_bIe-A"

bot = telebot.TeleBot(TOKEN)

conn = sqlite3.connect('translations.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS translations
                  (user_id INTEGER, original_text TEXT, translated_text TEXT, target_lang TEXT)''')
conn.commit()

@bot.message_handler(commands=['start'])
def handle_start(message): 
    bot.send_message(message.chat.id, 'Привет! Отправь голосовое сообщение, которое нужно перевести.') 



@bot.message_handler(commands=['language'])
def send_lang(message):
   
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn1 = types.InlineKeyboardButton("🇬🇧 Английский", callback_data='action1')
    btn2 = types.InlineKeyboardButton("🇨🇳 Китайский", callback_data='action2')
    btn3 = types.InlineKeyboardButton("🇪🇸 Испанский", callback_data='action3')
    btn4 = types.InlineKeyboardButton("🇫🇷 Французский", callback_data='action4')
    btn5 = types.InlineKeyboardButton("🇩🇪 Немецкий", callback_data='action5')
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    bot.send_message(message.chat.id, "Выберите язык:", reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
1. Отправь мне голосовое сообщение на русском языке
2. Я распознаю текст и переведу его на выбранный язык
3. Для выбора языка используй команду /language
4. Посмотреть историю переводов:\n /history

Доступные языки:
- 🇬🇧 Английский
- 🇨🇳 Китайский
- 🇪🇸 Испанский
- 🇫🇷 Французский
- 🇩🇪 Немецкий
    """
    bot.send_message(message.chat.id, help_text)


print('Сервер запущен.')
bot.polling(
    non_stop=True,
    interval=1  
)
