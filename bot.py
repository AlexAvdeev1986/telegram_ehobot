import telebot

token = '7106728452:AAEZuBbXJbCBSJxJ0r2n5mHCek8_jq8BeDA'  # Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()
