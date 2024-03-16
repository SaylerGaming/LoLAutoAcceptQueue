from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from asyncio import get_event_loop

TOKEN : Final = '6736595463:AAHB4szAPZfjbmkTteu73n3aHj1RT1t1dVg'
BOT_USERNAME: Final = '@LeagueNotifierBot'

async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Твой Chat ID: <code>{update.message.chat.id}</code>", parse_mode="html")
    get_event_loop().stop()

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', startCommand))

    print('starting bot...')
    app.run_polling(poll_interval=1)

if __name__ == '__main__':
    main()