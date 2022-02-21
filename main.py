import telebot

# токен
token = '5033996376:AAGmQxjIZHx8g8083zGTj6pZ7vR_PZwEq9k'
bot = telebot.TeleBot(token)
GROUP_ID=bot.get_chat('@test_moderapt').id
# Список запрещённых слов
blaclist=['бля','хуй','пизд','пидар','сука','суки','пидр','пидор','сучка','сучон','гондон','ебат','ебл','ебал']
momsave = ['мать твою ебал', 'еб твою мать','мамашу твою ебал', 'еб твою мамашу','мамку твою ебал', 'еб твою мамку',]


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Приветствую, /help для просмотра списка команд")

@bot.message_handler(commands=['help'])
def start_message(message):
  bot.send_message(message.chat.id,"/ban - блокировка пользователя \n /unban - разблокировка пользователя \n /start \n ВНИМАНИЕ пока я нахожусь в чате я буду автоматически удалять сообщения содержащие ненормативную лексику")

# команды для добавления слов в блеклист(ДОДЕЛАТЬ)
# @bot.message_handler(commands=['blacklist'])
# blaclist.append(message)
# def start_message(message):
#   bot.send_message(message.chat.id, "словарь пополнен")

@bot.message_handler(commands=['blacklist'])
def start_message(message):
	bot.send_message(message.chat.id, message.text)

# просмотр сообщений
@bot.message_handler(content_types=["text"])
def handle_text(message):
	for x in momsave:
		if(x in message.text):
			bot.delete_message(message.chat.id, message.message_id)
			bot.send_message(message.chat.id, "мама это святое, нельзя про неё так говорить")
			break
			
	for x in blaclist:
		if(x in message.text):
			# удаление сообщения с матом
			bot.delete_message(message.chat.id, message.message_id)
			bot.send_message(message.chat.id, " разговаривай без матов дуралей")
			break

if __name__ == '__main__':
	bot.infinity_polling()
