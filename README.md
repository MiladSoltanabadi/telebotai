# Telegram Bot with AI Chat using GPT-2 (Persian)

This project is a Telegram bot that uses the GPT-2 language model (fine-tuned for Farsi) to generate intelligent responses to user inputs. The bot automatically replies to user messages with contextually relevant and coherent answers.

## Description

This Telegram bot uses the `aiogram` library to interact with Telegram and the `transformers` library from Hugging Face to process natural language using a pre-trained GPT-2 model fine-tuned for the Farsi language. The bot listens for messages from users and generates responses based on the input using the GPT-2 model.

## Prerequisites

Before running the project, you need to install some required libraries and set up the environment.

### Install Dependencies

1. Install the required libraries using the following command:
   ```bash
   pip install aiogram transformers
   
2. If you need the torch library for model processing, install it with:
   ```bash
   pip install torch

3. Ensure you have Python 3.7 or higher installed.

## Set the Bot Token
To use the Telegram bot, you need to obtain a bot token from BotFather on Telegram and replace the placeholder in the code:
   ```bash
   API_TOKEN = 'Your-Bot-Token-Here'
```

## Set the Persian Language Model

This project uses the HooshvareLab/gpt2-fa model fine-tuned for the Farsi language. You can use similar models from Hugging Face. Set the model cache directory if needed(or better ones if you have access):
   ```bash
os.environ["TRANSFORMERS_CACHE"] = "path/to/cache/directory"
```
## Usage

1. Start the bot by sending the /start command.
2. The bot will automatically generate responses to any text you send using the GPT-2 model.

## Run the Bot

To run the bot, simply execute the following command in your terminal:
   ```bash
  python main.py
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.

