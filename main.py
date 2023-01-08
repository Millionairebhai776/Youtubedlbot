import pyrogram
import youtube_dl
from pyrogram import Client

# Replace "TOKEN" with your bot's token
api_id = 16393106
api_hash = "061fbf1aff7eecf2edb8434ddbab7a7d"
bot_token = "5900132667:AAHfAQfu6bGilLr8y2MvwwcH_sEBVPuq8jo"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message()
def download_video(client, message):
    # Make sure the message is a reply to the bot
    if message.reply_to_message:
        # Get the URL of the YouTube video
        url = message.text
        # Use youtube-dl to download the video
        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "outtmpl": "%(id)s.%(ext)s",
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        # Send the downloaded video back to the user
        client.send_document(
            message.chat.id,
            document=url.split("=")[-1] + ".mp4",
            reply_to_message_id=message.message_id,
        )

app.run()
