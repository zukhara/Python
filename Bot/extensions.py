# extensions.py
import telebot
import requests
import json
from config import TELEGRAM_BOT_TOKEN

class APIException(Exception):
    def __init__(self, message):
        self.message = message

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        url = f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}"
        response = requests.get(url)
        data = response.json()
        if quote in data:
            price = data[quote]
            result = price * amount
            return result
        else:
            raise APIException(f"Не удалось получить данные о валюте {quote}")

class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

    def start(self):
        @self.bot.message_handler(commands=['start', 'help'])
        def handle_start_help(message):
            instructions = "Привет! Я бот для конвертации валют. Для получения цены на валюту введите команду в формате:\n\n"
            instructions += "<имя валюты цену которой вы хотите узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>"
            instructions += "Примеры:\n"
            instructions += "/help - выводит эту справку\n"
            instructions += "/values - выводит список доступных валют\n"
            instructions += "Примеры конвертации:\n"
            instructions += "1. USD to EUR 100\n"
            instructions += "2. EUR to USD 50\n"
            instructions += "3. RUB to USD 1000"
            self.bot.send_message(message.chat.id, instructions)

        @self.bot.message_handler(commands=['values'])
        def handle_values(message):
            currencies = "Доступные валюты:\n\n"
            currencies += "1. Евро (EUR)\n"
            currencies += "2. Доллар (USD)\n"
            currencies += "3. Рубль (RUB)"
            self.bot.send_message(message.chat.id, currencies)

        @self.bot.message_handler(func=lambda message: True)
        def handle_currency_conversion(message):
            try:
                input_text = message.text.split()
                if len(input_text) != 4:
                    raise APIException("Неправильный формат команды. Используйте /help, чтобы узнать, как её правильно вводить.")
                
                base_currency, quote_currency, amount = input_text[0], input_text[2], float(input_text[3])
                converted_amount = CurrencyConverter.get_price(base_currency, quote_currency, amount)
                response_text = f"{amount} {base_currency} равно {converted_amount} {quote_currency}"
                self.bot.send_message(message.chat.id, response_text)
            except APIException as e:
                self.bot.send_message(message.chat.id, str(e))
            except ValueError:
                self.bot.send_message(message.chat.id, "Неправильно введено число.")
        
        self.bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    bot = TelegramBot()
    bot.start()