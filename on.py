import os
import telegram
from telegram.ext import Updater, CommandHandler

# Reemplaza 'TU_TOKEN' con el token real de tu bot de Telegram
TOKEN = '5634032110:AAF__7OdSweIftReXukx30rj7zKlgAIAld4'

# Función para el comando /onn
def on(update, context):
    try:
        # Obten el número del argumento
        num = int(context.args[0])

        # Ejecuta el comando python3 bot.py con el número como argumento
        os.system(f'python3 bot.py {num}')

        # Envía un mensaje de confirmación al usuario
        update.message.reply_text(f'Ejecutando bot.py con el número {num}')

    except (IndexError, ValueError):
        update.message.reply_text('Uso: /on [1-6]')

def main():
    # Inicializa el bot
    bot = telegram.Bot(token=TOKEN)
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Agrega el manejador del comando /on
    dispatcher.add_handler(CommandHandler('on', on, pass_args=True))

    # Inicia el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
