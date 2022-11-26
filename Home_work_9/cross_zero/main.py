# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

import logging
from mod_log import get_dir, LOG
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler, RegexHandler, messagequeue as mq

from mod_game import cross, zero, start_game

# API_KEY создается в BotFather в телеграме и привязывается к аккаунту
# потому тут его не размещаю, так как гитхаб публичный
from mod_settings import API_KEY

@LOG
def main():
    logging.basicConfig(format='%(asctime)s       %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename=get_dir()+'\\'+'botlog.txt')
    updater = Updater(API_KEY)

    updater.bot._msg_queue = mq.MessageQueue()
    updater.bot._is_messages_queued_default = True

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start_game", start_game)],

        states={
            "CHOOSING_X": [RegexHandler('^(1|2|3|4|5|6|7|8|9)$', cross)],
            "CHOOSING_O": [RegexHandler('^(1|2|3|4|5|6|7|8|9)$', zero)],
        },

        fallbacks=[MessageHandler(Filters.text, interceptor)]
    )

    dp.add_handler(conv_handler)

    # Запускаем бота
    updater.start_polling()

    # Бот работает все время до нажатия Ctrl-C или блокировки start_polling()
    updater.idle()

@LOG
def start(bot, update):
    text = 'Для того чтобы начать играть введите: /start_game. Если во время игры ввести "stop", то игра прервется'
    update.message.reply_text(text)

@LOG
def interceptor(bot, update):
    global board
    if update.message.text == "stop":
        return ConversationHandler.END
    else:
        update.message.reply_text("Некорректный ввод. Вы уверены, что ввели число от 1 до 9?")

if __name__ == '__main__':
    main()