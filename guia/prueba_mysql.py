from telegram.ext import Updater, CommandHandler, ConversationHandler
from mysql.connector import connect, errorcode, Error


try:
    cnx = connect(host='127.0.0.1', user='root', password='12345678', database='bot_telegram')
except Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuario o password incorrectos')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('La base de datos no existe')
    else:
        print(err)
else:
    pass


def start_handler(update, context):
    update.message.reply_text(text='Datos extraidos con mysql')
    #update.message.reply_text(text="""(▓▓▓░░░░░░░░░░░░░░░) 15%""")
    cursor = cnx.cursor()
    cursor.execute("select id, balance, fecha from users")
    users = cursor.fetchall()
    for u in users:
        a = u[0]
        b = u[1]
        c = u[2]
        #print(f'ID: {a}  Balance: {b} Fecha: {c}')
        update.message.reply_text(text=f'ID: {a}  Balance: {b} Fecha: {c}')


def main():

    updater = Updater(token='2023064956:AAEx0eGNieLWH9fNKTVG7_FG0UhoYaxTxXY', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('start', start_handler)
        ],
        states={},
        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()

    print('Bot en ejecucion')



if __name__ == '__main__':
    main()
