from telebot.types import Chat
import telebot, requests, json


TOKEN = "BOT_TOKEN" # Put your bot token instead of BOT_TOKEN


def gpt(msg):
    url = f'https://api.voidevs.com/gpt/free?msg={msg}'
    try:
        respons = requests.get(url)
        if respons.status_code == 200:
            response_text = respons.text
            response_dict = json.loads(response_text)
            if response_dict['result']:
                return response_dict['results']['answer']
            else:
                return False
        else:
            return False
    except:
        return False


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, welcome to ChatGPT free bot")


@bot.message_handler(func=lambda message: True)
def keyboard(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        if message.text.startswith('//'):
            text = message.text[2:]
            answer = gpt(text)
            if answer:
                bot.reply_to(message, answer)
            else:
                bot.reply_to(message, "Sorry, I don't have the ability to answer your question now!")
    else:
        answer = gpt(message.text)
        if answer:
            bot.reply_to(message, answer)
        else:
            bot.reply_to(message, "Sorry, I don't have the ability to answer your question now!")
    

bot.polling()
