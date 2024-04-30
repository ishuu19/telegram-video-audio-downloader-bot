# Telegram Media Downloader Bot

This Telegram bot allows users to download media (audio or video) from YouTube by simply sending the video link and specifying their preferred format.

## Features

- **Simple Interface**: Users interact with the bot by sending a YouTube video link and choosing between audio or video download options.
- **Flexible Download Options**: Supports downloading both audio and video formats in the best available quality.
- **Error Handling**: Includes robust error handling to gracefully handle any issues that may arise during the download process.
- **Conversation Handling**: Utilizes the Telegram ConversationHandler to guide users through the download process seamlessly.
- **File Cleanup**: Automatically removes downloaded media files from the server after sending them to the user.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/telegram-media-downloader.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the required environment variables:

    - `TELEGRAM_API_TOKEN`: Your Telegram Bot API token.
    - `FFMPEG_LOCATION`: File path to the ffmpeg executable.
    - `FFPROBE_LOCATION`: File path to the ffprobe executable.

## Usage

1. Start the bot by running the main Python script:

    ```bash
    python main.py
    ```

2. In your Telegram client, start a conversation with the bot by sending the `/start` command.

3. Send the bot the YouTube video link you want to download.

4. Choose between downloading the audio or video format when prompted.

5. Wait for the bot to process your request and send you the downloaded media file.

## Configuration

- **Telegram API Token**: Replace `"YOUR_TELEGRAM_API_TOKEN"` in the `main.py` script with your actual Telegram Bot API token.
- **FFmpeg and FFprobe Locations**: Update the `ffmpeg_location` and `ffprobe_location` variables in the `download_media` function of the `main.py` script with the file paths to the `ffmpeg` and `ffprobe` executables on your system.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This bot was developed using the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library.
- Media downloading is facilitated by the [yt-dlp](https://github.com/yt-dlp/yt-dlp) library.
