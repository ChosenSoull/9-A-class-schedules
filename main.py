import telebot
from telebot import types

answers = {
    "понедельник": "Расписание на понедельник:\nФізика\nФізика\nГеометрія\nУкраїнська мова\nАнглійська мова\nФізична культура\nОснови правознавства",
    "вторник": "Расписание на вторник:\nХімія\nХімія\nТрудове навчання\nАлгебра\nАлгебра\nФізична культура\nУкраїнська література",
    "среда": "Расписание на среду:\nОснови здоров’я\nВсесвітня історія\nМистецтво\nАнглійська мова\nУкраїнська мова\nГеографія\nГеографія",
    "четверг": "Расписание на четверг:\nІсторія України\nІсторія України\nУкраїнська література\nАнглійська мова\nГеометрія\nБіологія\nБіологія",
    "пятница": "Расписание на пятницу:\nАлгебра\nФізика\nІнформатика\nІнформатика\nФізична культура\nЗарубіжна література\nЗарубіжна література",
}

bot = telebot.TeleBot("YouTelegramBotToken")	

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Показать расписание')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Привет! Хочешь узнать расписание?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()

    if text == 'показать расписание':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for day in answers:
            markup.add(types.KeyboardButton(day))
        bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=markup)
    elif text in answers:  # Проверяем, есть ли введенный день в словаре
            bot.send_message(message.chat.id, answers[text])

bot.infinity_polling()
