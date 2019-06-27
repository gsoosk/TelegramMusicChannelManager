# Telegram Music Channel Manager

## What is it ? 
It's a simple bot to manage your music channel. With just adding this bot to your channel, it automatically adds audio details in it's caption with bellow format.
```
✏️ Title: <title>
👤 Artist: <artist>
💽 Album: <album>
🎼 Genre: <genre>
```

<img src="https://github.com/gsoosk/TelegramMusicChannelManager/blob/master/demo.png" width="450" />


## How to run ? 
First of all you should add your bot `TOKEN` to config file.

### Manual
You should firt install requirements.
* `python 3`
* `python-telegram-web`
* `mutagen`

To install them just run this command.
```
pip install --no-cache-dir -r requirements.txt
```
Then you can run program with this command.
```
python main.py
```
### Docker
[![Docker Repository on Quay](https://quay.io/repository/gsoosk/telegram_channel_music_manager/status "Docker Repository on Quay")](https://quay.io/repository/gsoosk/telegram_channel_music_manager)


You can run docker image just with this command : 
```
docker run --name <container_name> quay.io/gsoosk/telegram_channel_music_manager 
```


