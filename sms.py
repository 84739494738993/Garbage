import telebot
from datetime import date
import os
from dotenv import load_dotenv
from datetime import datetime


def get_date():
    list_day_zmieszane   = [6,20,6,20]
    list_day_segregacja   = [25,25]
    list_day_bioodpady   = [5,19,5,19]
    list_day_gabaryty   = [0]
    list_month_zmieszane   = [2,2,3,3]
    list_month_segregacja   = [2,3]
    list_month_bioodpady   = [2,2,3,3]
    list_month_gabaryty   = [0]
    today = date.today()
    now = datetime.now()
    day = today.day
    month = today.month
    Answer = []
    for i in range(len(list_day_zmieszane)):
        if list_day_zmieszane[i]==day+1 and list_month_zmieszane[i]==month and now.hour > 16:
            Answer.append(f'Dobry wieczór 🌑, mamo, jutro są: zmieszane 🟢🗑️🍄‍🟫🍞🌽🍓')
        elif list_day_zmieszane[i]==day and list_month_zmieszane[i]==month and now.hour < 8:
            Answer.append(f'Dobry ranok 🌞, mamo, dzisiaj są: zmieszane 🟢🗑️🍄‍🟫🍞🌽🍓 trzeba biec 🏃‍♀️!!!')
    for i in range(len(list_day_segregacja)):
        if list_day_segregacja[i]==day+1 and list_month_segregacja[i]==month and now.hour > 16:
            Answer.append(f'Dobry wieczór 🌑, mamo, jutro jest: segregacja 🟡🗑️📃📖📰🚽')
        elif list_day_segregacja[i]==day and list_month_segregacja[i]==month and now.hour < 8:
            Answer.append(f'Dobry ranok 🌞, mamo, dzisiaj jest: segregacja 🟡🗑️📃📖📰🚽 trzeba biec 🏃‍♀️!!!')
    for i in range(len(list_day_bioodpady)):
        if list_day_bioodpady[i]==day+1 and list_month_bioodpady[i]==month and now.hour > 16:
            Answer.append(f'Dobry wieczór 🌑, mamo, jutro są: bioodpady 🟤🗑️🥑🍌🧅🌰')
        elif list_day_bioodpady[i]==day and list_month_bioodpady[i]==month and now.hour < 8:
            Answer.append(f'Dobry ranok 🌞, mamo, dzisiaj są: bioodpady 🟤🗑️🥑🍌🧅🌰 trzeba biec 🏃‍♀️!!!')            
    for i in range(len(list_day_gabaryty)):
        if list_day_gabaryty[i]==day+1 and list_month_gabaryty[i]==month and now.hour > 16:
            Answer.append(f'Dobry wieczór 🌑, mamo, jutro są: gabaryty 🟠🗑️🚪🚽🛁📺')
        if list_day_gabaryty[i]==day and list_month_gabaryty[i]==month and now.hour < 8:
            Answer.append(f'Dobry ranok 🌞, mamo, dzisiaj są: gabaryty 🟠🗑️🚪🚽🛁📺 trzeba biec 🏃‍♀️!!!')
    return Answer

if __name__ == '__main__':
    get_date()

load_dotenv()

# Получаем токен и chat_id из переменных окружения
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHANNEL_ID')  # или TELEGRAM_CHAT_ID

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)
now = datetime.now()
# Сообщение
print(*get_date())
# Отправка сообщения
if len(get_date())>0:
    for i in get_date():
        TEXT = i
else:
    if now.hour < 12:
        TEXT = f'Dobry ranok 🌞, mamo, dzisiaj niema nic 🎉 - można odpocząć 💤!!!'
    elif now.hour >= 17:
        TEXT = f'Dobry wieczór 🌑, mamo, jutro niema nic 🎉 - można odpocząć 💤!!!'
bot.send_message(CHAT_ID, TEXT)
