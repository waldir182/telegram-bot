from telegram.ext import Updater, CommandHandler, ConversationHandler
from db.db_users import usuario_existe
import os

def start_handler(update, context):
    update.message.reply_text(text='Hola bienvenido!!!')
    if usuario_existe(update):
        update.message.reply_text(text='Usted ya esta registrado')
    else:
        update.message.reply_text(text='Aun por registrar')


def main():
    updater = Updater(token=os.environ['TOKEN'], use_context=True)
    dispacher = updater.dispatcher

    dispacher.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('start', start_handler)
        ],
        states={},
        fallbacks=[]
    ))

    print('Bot ejecutandose')
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
