from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import json
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

with open("config.json", "r") as read_file:
    config = json.load(read_file)


updater = Updater(config["TOKEN"])
dispatcher = updater.dispatcher




def change_caption(bot, update):
    logging.log(logging.INFO, "Changing caption")
    chat_id = update.effective_message.chat_id
    message_id = update.effective_message.message_id
    bot.edit_message_caption(chat_id=chat_id, message_id=message_id, caption="salam")


handler = MessageHandler(Filters.audio, change_caption, channel_post_updates=True, message_updates=False)
# handler = CommandHandler("ok", echo)
dispatcher.add_handler(handler=handler)



POLLING_INTERVAL = 0.2
updater.start_polling(poll_interval=POLLING_INTERVAL)
updater.idle()