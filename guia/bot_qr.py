from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, \
    MessageHandler, Filters
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup
import qrcode
import os

INPUT_TEXT = 0


def start(update, context):
    button1 = InlineKeyboardButton(text='Generar codigo QR', callback_data='qr')
    button2 = InlineKeyboardButton(text='Boton de rrelleno', url='https://youtube.com')

    update.message.reply_text(
        text='Hola soy tu bot de qr\n\nUtiliza /qr para generar un QR',
        reply_markup=InlineKeyboardMarkup([
            [button1],
            [button2]
        ])
    )


def generar_qr(text):
    filename = text + '.jpg'
    img = qrcode.make(text)
    img.save(filename)
    return filename


def send_qr(filename, chat):
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    chat.send_photo(
        photo=open(filename, 'rb')
    )
    os.unlink(filename)


def input_text(update, context):
    text = update.message.text
    filename = generar_qr(text)
    chat = update.message.chat
    send_qr(filename, chat)
    return ConversationHandler.END


def qr_command_handler(update, context):
    update.message.reply_text('Enviame un un texto para genera en codigo QR')
    return INPUT_TEXT


def qr_callback_handler(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text( text='Enviame un un texto para genera en codigo QR' ) #remplazar
    query.message.reply_text(text='Enviame un un texto para genera en codigo QR')
    return INPUT_TEXT


if __name__ == '__main__':

    updater = Updater(token='2023064956:AAEx0eGNieLWH9fNKTVG7_FG0UhoYaxTxXY', use_context=True)
    dispacher = updater.dispatcher

    start_handler = CommandHandler('start', start)

    dispacher.add_handler(start_handler)
    dispacher.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr', qr_command_handler),
            CallbackQueryHandler(pattern='qr', callback=qr_callback_handler)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },
        fallbacks=[],
        per_message=True
    ))

    updater.start_polling()
    updater.idle()