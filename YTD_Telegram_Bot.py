from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CommandHandler
import os
import yt_dlp

# Define states
CHOOSING, TYPING_REPLY = range(2)

# Function to handle incoming messages
def start(update, context):
    context.user_data['link'] = None
    context.user_data['choice'] = None
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Send me the link of the video you want to download.")
    return CHOOSING

def regular_choice(update, context):
    text = update.message.text
    context.user_data['link'] = text
    update.message.reply_text("Choose what you want to download: audio or video?")
    return TYPING_REPLY

def received_information(update, context):
    choice = update.message.text.lower()
    context.user_data['choice'] = choice
    update.message.reply_text(f"You chose to download {choice}. Please wait a moment.")
    download_media(update, context)
    context.user_data['link'] = None
    context.user_data['choice'] = None
    return CHOOSING

def download_media(update, context):
    url = context.user_data['link']
    choice = context.user_data['choice']
    try:
        # Set the location of ffmpeg and ffprobe
        ffmpeg_location = "D:/ffmpeg-master-latest-win64-gpl/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe"
        ffprobe_location = "D:/ffmpeg-master-latest-win64-gpl/ffmpeg-master-latest-win64-gpl/bin/ffprobe.exe"

        # Download the media (audio or video) in the best available quality
        ydl_opts = {'format': 'best', 'ffmpeg_location': ffmpeg_location, 'ffprobe_location': ffprobe_location}
        if choice == 'audio':
            ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
        elif choice == 'video':
            ydl_opts['postprocessors'] = [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}]
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir('.'):
            if file.endswith(('mp4', 'webm', 'mp3')):
                media_file = file
                break

        context.bot.send_document(chat_id=update.effective_chat.id, document=open(media_file, 'rb'))

        os.remove(media_file)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Sorry, an error occurred while processing the request.")

    return

def cancel(update, context):
    context.user_data['link'] = None
    context.user_data['choice'] = None
    return ConversationHandler.END

def main():
    updater = Updater("TOKEN", use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [MessageHandler(Filters.text & ~Filters.command, regular_choice)],
            TYPING_REPLY: [MessageHandler(Filters.text & ~Filters.command, received_information)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )


    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('start', start))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
