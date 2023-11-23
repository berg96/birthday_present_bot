import os

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()
TOKEN = os.getenv('TOKEN')
HI_MESSAGE = 'Привет, {name}. Здесь краткое описание возможностей бота'
TEXT_MESSAGE = (
    'Пока я не могу тебе ответить, '
    'но ты можешь выбрать команды снизу или написать /help'
)


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=TEXT_MESSAGE)


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup(
        [
            ['/newbday', '/newpresent']
        ],
        resize_keyboard=True
    )
    context.bot.send_message(
        chat_id=chat.id,
        text=HI_MESSAGE.format(name=name),
        reply_markup=buttons
    )


def main():
    print('hi')
    updater = Updater(token=TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
