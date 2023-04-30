from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, Update, WebAppInfo, KeyboardButton
from telegram.ext import (
	Application,
	CommandHandler,
	ContextTypes,
	ConversationHandler,
	MessageHandler,
	filters,    
)

import json

TOKEN = ""

START, ASK, CONNECT, WAIT = range(4)

def receive_message(update):

    # Getting data from keyboard or message
    if update.callback_query:
        text = update.callback_query.data
        print(text)
    else:
        text = update.message.text.replace('\n','\\n')
        print(text)
    # If this user has been logged in chats
    # if update.effective_chat.id in chats:
    #     user = chats[update.effective_chat.id]
    #     #user.last_seen = datetime.now()
    #     #.logger.info('Logging - %s - %s received: %s' % (update.effective_chat.id, user.email, text))
    #     print('Logging - %s received: %s' % (update.effective_chat.id, text))
    #     return user
    # else:
    #     logger.info('Logging - %s received: %s' % (update.effective_chat.id, text))





async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

	# receive_message(update)
    await update.message.reply_text("Welcome to SetTlE",reply_markup=ReplyKeyboardRemove())
    
    receive_message(update)
    

	# Code some logic to check if the user has to recieve, check if it's screen name instead
	# if update.effective_chat.id in db:
    await update.message.reply_text(
		"Siddarth has requested you pay!" ,
        reply_markup = ReplyKeyboardMarkup.from_button(
            KeyboardButton(
                text="Click to connect wallet"),
                web_app=WebAppInfo(url="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwi7vu3i7dH-AhVKi1wKHab2DMUQtwJ6BAgLEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ&usg=AOvVaw0aHtehaphMhOCAkCydRLZU"),
        )
	)
	# 	# Keyboard here
	# 	return EXIT

	# await update.message.reply_text("Type $ amount for payment")
    return START



async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	# receive_message(update)
	await update.message.reply_text("Wait")
	return WAIT

def main() -> None:
	"""Run the bot."""
	# Create the Application and pass it your bot's token.
	application = Application.builder().token(TOKEN).build()

	# Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
	conv_handler = ConversationHandler(
		entry_points=[CommandHandler("start", start)],
		states={
			START: [MessageHandler(filters.ALL, start)],
			# CONNECT: [MessageHandler(filters.ALL, connect)],
			# ASK: [MessageHandler(filters.ALL, connect)],
			# LOCATION: [
			# 	MessageHandler(filters.LOCATION, location),
			# 	CommandHandler("skip", skip_location),
			# ],
			# BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, bio)],
		},
		fallbacks=[CommandHandler("cancel", cancel)],
	)

	application.add_handler(conv_handler)
            

	application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))
	# application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))

	# Run the bot until the user presses Ctrl-C
	application.run_polling()


async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Print the received data and remove the button."""

    # Here we use `json.loads`, since the WebApp sends the data JSON serialized string

    # (see webappbot.html)

    data = json.loads(update.effective_message.web_app_data.data)

    await update.message.reply_html(

        text=f"You selected the color with the HEX value <code>{data['hex']}</code>. The "

        f"corresponding RGB value is <code>{tuple(data['rgb'].values())}</code>.",

        reply_markup=ReplyKeyboardRemove(),

    )

if __name__ == "__main__":
	main()
