import telebot
from datetime import date
import os
from dotenv import load_dotenv


def get_date():
    list_day_zmiszane   = [7,21,7,21,4,18,2,16,30,13,27,11,25,8,22,5,19,3,17,31,14,28,12,27,9,23]
    list_day_segregacja   = [26,26,23,21,18,16,13,10,8,5,3,31,28]
    list_day_bioodpady   = [6,20,6,20,3,17,26,15,29,12,26,10,24,7,21,4,18,2,16,30,13,27,11,20,8,22]
    list_day_gabaryty   = [3,16]
    list_month_zmiszane   = [2,2,3,3,4,4,5,5,5,6,6,7,7,8,8,9,9,10,10,10,11,11,12,12,1,1]
    list_month_segregacja   = [2,3,4,5,6,7,8,9,10,11,12,1]
    list_month_bioodpady   = [2,2,3,3,4,4,4,5,5,6,6,7,7,8,8,9,9,10,10,10,11,11,12,12,1,1]
    list_month_gabaryty   = [4,10]

    today = date.today()
    day = today.day
    month = today.month
    Answer = []
    for i in range(len(list_day_zmiszane)):
        if list_day_zmiszane[i]==day+1 and list_month_zmiszane[i]==month:
            Answer.append("zmiszane")
    for i in range(len(list_day_segregacja)):
        if list_day_segregacja[i]==day+1 and list_month_segregacja[i]==month:
            Answer.append("segregacja")
    for i in range(len(list_day_bioodpady)):
        if list_day_bioodpady[i]==day+1 and list_month_bioodpady[i]==month:
            Answer.append("bioodpady")
    for i in range(len(list_day_gabaryty)):
        if list_day_gabaryty[i]==day+1 and list_month_gabaryty[i]==month:
            Answer.append("gabaryty")
    return Answer

if __name__ == '__main__':
    get_date()

load_dotenv()

# Получаем токен и chat_id из переменных окружения
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHANNEL_ID')  # или TELEGRAM_CHAT_ID

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Сообщение
TEXT = get_date()
print(*get_date())
# Отправка сообщения
bot.send_message(CHAT_ID, TEXT)

