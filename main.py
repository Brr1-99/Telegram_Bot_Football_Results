import os, telebot
from loadDatas import loadData
from dotenv import load_dotenv

load_dotenv()

leagues_id = {
    "Premier_League": 39,
    "Ligue_1": 61,
    "Bundesliga": 78,
    "Serie_A": 135,
    "La_Liga" : 140,
}

API_KEY = os.getenv("BOT_API")

bot = telebot.TeleBot(token=API_KEY)

# Displays the information related to the bot
@bot.message_handler(commands=['start'])
def explain_bot(message):
    bot.send_message(message.chat.id,
    "This bot shows the standings for the most popular football leagues. \n" + 
    "Type command /help in order to get more information about how to do it."
    )

# Displays the commands you can use
@bot.message_handler(commands=['help'])
def get_data(message):
    bot.send_message(message.chat.id,
    """
    In order to get the standings type: /stand <<league>> \nwhere 'league' is the name of the competition you are looking for.\nType /leagues to get all names available. 
    """
    )

# Displays the leagues available
@bot.message_handler(commands=['leagues'])
def get_data(message):
    response = "Available leagues: \n"
    for name in leagues_id.keys():
        response += f"{name} \n"
    bot.send_message(message.chat.id, response)

# Displays the information about the selected league
@bot.message_handler(commands=['stand'])
def explain_bot(message):
    name = message.text.split()[1]
    if name:
        bot.send_message(message.chat.id,
        loadData(league=leagues_id[name] )
        )
    else:
        bot.send_message(message.chat.id,
        "Please write the name of the competition\nType /leagues to get all names available"
        )

bot.polling()