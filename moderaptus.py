import telebot

# токен
token = '5033996376:AAGmQxjIZHx8g8083zGTj6pZ7vR_PZwEq9k'
bot = telebot.TeleBot(token)
GROUP_ID=bot.get_chat('@test_moderapt').id
# Список запрещённых слов
blaclist=['бля','хуй','пизд','пидар','сука','суки','пидр','пидор','сучка','сучон']

# просмотр сообщений
@bot.message_handler(content_types=["text"])
def handle_text(message):
	for x in blaclist:
		if(x in message.text):
			# удаление сообщения с матом
			bot.delete_message(message.chat.id, message.message_id)
			break

if __name__ == '__main__':
	bot.infinity_polling()