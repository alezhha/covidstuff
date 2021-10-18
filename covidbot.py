import telebot
import requests
import datetime

covid_API = "https://covid-api.mmediagroup.fr/v1/cases"

covid = requests.get(covid_API)
covid_json = covid.json()

token = "2057282859:AAHicVGGSmtEfdhAu5InUMW0yX4UcZHtOuI"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "старт"])
def start(message):
    bot.send_message(message.chat.id, "Привтсвую, я - бот что помогает вам мониторить ситуацию с Covid-19 во всем мире. Для того чтобы узнать количество заболевших в вашей стране, просто введите её название.")


@bot.message_handler(content_types="text")
def countryname(message):
    country = message.text
    date = datetime.date.today()
    bot.send_message(message.chat.id, f"За сегодня, ({date.year}/{date.month}/{date.day}) В {country} выявлено {covid_json[f'{country.title()}']['All']['confirmed']} случаев заражения; Смертей - {covid_json[f'{country}']['All']['deaths']}.")


print('1')
bot.infinity_polling()