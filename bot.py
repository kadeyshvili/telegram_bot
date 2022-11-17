import telebot as telebot
from telebot import custom_filters, types
from telebot.types import Message

TOKEN = '5644900291:AAEHGq1ocCObAVcpVRS9vf6RA2V9W2sQ_Bg'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['hello_message'])
def hello_message(message):
    bot.send_message(message.chat.id, 'welcome to hell')


@bot.message_handler(commands=['buttons', 'clear_all'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton("Show statistics")
    markup.add(item_1)
    item_2 = types.KeyboardButton("Promote myself")
    markup.add(item_2)
    item_3 = types.KeyboardButton("🎲 Find out answer to your question")
    markup.add(item_3)
    item_4 = types.KeyboardButton("Everybody at AMI")
    markup.add(item_4)
    item_5 = types.KeyboardButton("Bot leave chat")
    markup.add(item_5)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(commands=['ban'])
def kick_member(message: [telebot.types.Message]):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    bot.restrict_chat_member(chat_id, user_id)


@bot.message_handler(commands=['unban'])
def kick_member(message: [telebot.types.Message]):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    bot.promote_chat_member(chat_id, user_id, can_delete_messages=True, can_post_messages=True,
                            can_edit_messages=True)


@bot.message_handler(commands=['promote'])
def promote_myself(message: [telebot.types.Message]):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    bot.promote_chat_member(chat_id, user_id, can_change_info=True, can_invite_users=True, can_delete_messages=True,
                            can_restrict_members=True, can_pin_messages=True, can_promote_members=True,
                            can_manage_chat=True, can_manage_video_chats=True, can_manage_voice_chats=True)


@bot.message_handler(content_types=['new_chat_members'])
def new_member(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    chat_id = message.chat.id
    user_name = message.new_chat_members[0].first_name
    bot.send_message(chat_id, f"Hi, {user_name}")


@bot.message_handler(content_types=['text'], text=['Promote myself'])
def promote_myself(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.promote_chat_member(chat_id, user_id, can_change_info=True, can_invite_users=True, can_delete_messages=True,
                            can_restrict_members=True, can_pin_messages=True, can_promote_members=True,
                            can_manage_chat=True, can_manage_video_chats=True, can_manage_voice_chats=True)


@bot.message_handler(content_types=['text', 'emoji'], text=['🎲 Find out answer to your question'])
def promote_myself(message: Message):
    chat_id = message.chat.id
    user_name = message.from_user.username
    r = bot.send_dice(message.chat.id)
    answers = ["definitely yes!", "you should think more about it", "no way that will work", "better not tell you now",
               "it is certain", "cannot predict now"]
    bot.send_message(chat_id, f"{user_name}, {answers[r.dice.value - 1]}")


@bot.message_handler(content_types=['text'], text=['Everybody at AMI'])
def show_pic(message: Message):
    dog = 'https://memepedia.ru/wp-content/uploads/2018/01/мем-this-is-fine.png'
    bot.send_message(message.chat.id, dog)


@bot.message_handler(content_types=['text'], text=['Show statistics'])
def show_statistics(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num_members = bot.get_chat_members_count(message.chat.id)
    admins = bot.get_chat_administrators(message.chat.id)
    cnt = 0
    for admin in admins:
        cnt += 1
    bot.send_message(message.chat.id, f"There are {num_members} members and {cnt} admins in this chat",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'], text=['Bot leave chat'])
def ban_member(message: Message):
    bot.leave_chat(message.chat.id)


if __name__ == '__main__':
    bot.add_custom_filter(custom_filters.TextMatchFilter())
    bot.polling(none_stop=True, interval=0)
