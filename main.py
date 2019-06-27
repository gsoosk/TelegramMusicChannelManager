from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import json
import logging
from mutagen.mp3 import MP3

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

with open("config.json", "r") as read_file:
    config = json.load(read_file)


updater = Updater(config["TOKEN"])
dispatcher = updater.dispatcher

class Audio:
    def __init__(self, bot, update):
        self.bot = bot
        self.update = update
        self.chat_id = update.effective_message.chat_id
        self.message_id = update.effective_message.message_id
        self.audio = self.download_audio()

    def download_audio(self):
        audio = self.update.effective_message.effective_attachment
        file_id = audio.file_id
        new_file = self.bot.get_file(file_id)

        logging.log(logging.INFO, "Downloading file")
        self.bot.edit_message_caption(chat_id=self.chat_id, message_id=self.message_id, caption="downloading...")

        new_file.download('file.mp3')
        logging.log(logging.INFO, "File downloaded")

        return MP3('file.mp3')

    def set_new_caption(self):
        title = self.audio.tags["TIT2"]
        artist = self.audio.tags["TPE1"]
        album = self.audio.tags["TALB"]
        genre = self.audio.tags["TCON"]

        new_caption = '''✏️ Title: {0}
👤 Artist: {1}
💽 Album:  {2}
🎼 Genre: {3}'''.format(title, artist, album, genre)

        self.bot.edit_message_caption(chat_id=self.chat_id, message_id=self.message_id, caption=new_caption)
        logging.log(logging.INFO, "Caption changed")


def change_caption(bot, update):
    logging.log(logging.INFO, "Changing caption")
    chat_id = update.effective_message.chat_id
    message_id = update.effective_message.message_id

    audio = Audio(bot, update)
    audio.set_new_caption()



handler = MessageHandler(Filters.audio, change_caption, channel_post_updates=True, message_updates=False)
# handler = CommandHandler("ok", echo)
dispatcher.add_handler(handler=handler)



POLLING_INTERVAL = 0.2
updater.start_polling(poll_interval=POLLING_INTERVAL)
updater.idle()