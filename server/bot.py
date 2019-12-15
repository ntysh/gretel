# создаем телеграм бота
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import Bot, ReplyKeyboardMarkup, KeyboardButton
from telegram.utils.request import Request

import config, core

req = Request(proxy_url=config.proxy)
bot = Bot(config.token, request=req)
upd = Updater(bot=bot, use_context=True)
dp = upd.dispatcher

# логирование
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# приветственное сообщение
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет! Через этого бота вы можете подписаться на срочные уведомления о том, что ваш друг попал в беду. Для этого введите команду /subscribe, а затем введите идентификатор этого человека. Если этот человек нажмет на свою кнопку тревоги, вам придет срочное оповещение.".format(config.name))

def subscribe(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Введите личный идентификатор человека, на оповещения которого вы хотите подписаться.")
    return "token"
    
def parse_token(update, context):

    try:
        core.subscribe_to_token(update.message.text, update.message.from_user.id)
        context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Спасибо! Теперь вы подписаны на этого человека. Если с ним что-то случится, вам придет сообщение и его координаты.")

    except IndexError:
        context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вы ввели неправильный токен. Попробуйте заново.")
    #else:
        
    return ConversationHandler.END	

# добавляем приветственное сообщение при команде старт


dp.add_handler(CommandHandler('start', hello))
dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('subscribe', subscribe)],

        states={
            "token": [MessageHandler(Filters.text, parse_token, pass_user_data=True)]
        },
        
        fallbacks = []
    ))

def main():
    upd.start_polling()
    upd.idle()

if __name__ == '__main__':
    main()
