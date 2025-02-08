from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import requests

# 替换为你的API Key和Bot Token
API_KEY = 'API_KEY'
TELEGRAM_BOT_TOKEN = 'BOT_TOKEN'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I'm your DeepSeek bot. How can I assist you today?")

async def handle_message(update: Update, context: CallbackContext) -> None:
    message = update.message.text

    # 替换prompt的内容
    prompt = (
        "PROMPT"
    )

    payload = {
        "model": "deepseek-ai/DeepSeek-V3",
        "messages": [
            {
                "role": "user",
                "content": prompt + message
            }
        ],
        "stream": False,
        "max_tokens": 512,
        "stop": ["null"],
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": {"type": "text"},
        "tools": [
            {
                "type": "function",
                "function": {
                    "description": "<string>",
                    "name": "<string>",
                    "parameters": {},
                    "strict": False
                }
            }
        ]
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.siliconflow.cn/v1/chat/completions", json=payload, headers=headers)

    # 检查API响应状态码和内容
    if response.status_code != 200:
        await update.message.reply_text(f"API request failed with status code: {response.status_code}")
        return

    response_data = response.json()

    if 'choices' not in response_data:
        await update.message.reply_text("API response does not contain 'choices'")
        return

    reply = response_data['choices'][0]['message']['content']
    await update.message.reply_text(reply)

def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()