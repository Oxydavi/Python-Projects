import telebot
from telebot import types
import requests
import random

bot = telebot.TeleBot('your toeken')
WEATHER_API_KEY = "your toeken"
COINMARKETCAP_API_KEY = "your toeken"
helplist = "/help - список команд"\
           "\n/hello - поздороваться" \
           "\n/website - сайт " \
           "\n/id - узнать свой id " \
           "\n/photo - получить своё фото" \
           "\n/weather город - получить информацию о погоде в городе"\
           "\n/hot - Орёл или решка"


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, helplist, parse_mode='html')


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "И тебе хеллоу", parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://ru.wikipedia.org/wiki/%D0%A0%D0%B8%D0%BA%D1"
                                                               "%80%D0%BE%D0%BB%D0%BB%D0%B8%D0%BD%D0%B3"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)


@bot.message_handler(commands=['id'])
def idcheck(message):
    bot.send_message(message.chat.id, f"Твой id: {message.from_user.id}", parse_mode='html')


@bot.message_handler(commands=['photo'])
def photo(message):
    phot = open('123.jpg', 'rb')
    bot.send_photo(message.chat.id, phot)


@bot.message_handler(commands=['weather'])
def send_weather(message):
    try:
        city = message.text.split()[1]
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            weather_description = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            reply = f'Погода в городе {city}:\nОписание: {weather_description}\n' \
                    f'Температура: {temp}°C\nВлажность: {humidity}%\n' \
                    f'Скорость ветра: {wind_speed} м/c'
        else:
            reply = 'Не удалось получить данные о погоде'

        bot.reply_to(message, reply)
    except:
        pass


@bot.message_handler(commands=['bc'])
def get_bitcoin_price(message):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY
    }
    parameters = {
        'symbol': 'BTC'
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    if 'data' in data:
        price = data['data']['BTC']['quote']['USD']['price']
        reply = f'Текущий курс биткоина: ${price:.2f}'
    else:
        reply = 'Не удалось получить данные о курсе биткоина'

    bot.reply_to(message, reply)


@bot.message_handler(commands=['eth'])
def get_ethereum_price(message):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY
    }
    parameters = {
        'symbol': 'ETH'
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    if 'data' in data:
        price = data['data']['ETH']['quote']['USD']['price']
        reply = f'Текущий курс эфириума: ${price:.2f}'
    else:
        reply = 'Не удалось получить данные о курсе эфириума'

    bot.reply_to(message, reply)


@bot.message_handler(commands=['hot'])
def hot(message):
    result = random.randint(1, 2)
    if result == 1:
        bot.send_message(message.chat.id, "Орёл", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Решка", parse_mode='html')


bot.polling(none_stop=True)
