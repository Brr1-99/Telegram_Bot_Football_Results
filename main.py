import os, telebot
from loadDatas import loadData
from dotenv import load_dotenv

load_dotenv()

leagues_id = {
    "Premier League": 39,
    "Ligue 1": 61,
    "Bundesliga": 78,
    "Serie A": 135,
    "La Liga" : 140,

}

API_KEY = os.getenv("BOT_API")

bot = telebot.TeleBot(token=API_KEY)

@bot.message_handler(commands=['start'])
def explain_bot(message):
    bot.send_message(message.chat.id,
    "This bot shows the standings for the most popular football leagues. \n" + 
    "Type command /help in order to get more information about how to do it."
    )

@bot.message_handler(commands=['help'])
def get_data(message):
    bot.send_message(message.chat.id,
    """
    In order to get the standings type: <<league>> \nwhere 'league' is the name of the competition you are looking for.\nType /leagues to get all names available. 
    """
    )

@bot.message_handler(commands=['leagues'])
def get_data(message):
    response = "Available leagues: \n"
    for name in leagues_id.keys():
        response += f"{name} : {'_'.join(name.split(' '))} \n"
    bot.send_message(message.chat.id, response)

bot.polling()

# for id in leagues_id:
#     data = loadData(league=id)
