from fastapi import FastAPI, Request, HTTPException
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
from dotenv import load_dotenv
import routers.hooker as hooker

# Load environment variables
load_dotenv()
CHANNEL_SECRET = os.getenv("CHANNEL_SECRET")
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
BASE_URL = os.getenv("BASE_URL")

# Initialize FastAPI app
app = FastAPI()

# Initialize LINE Bot API and Webhook Handler
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# Test for server status
@app.get(BASE_URL)
async def root():
    return {"status": "Server is running"}

# Webhook callback endpoint
app.include_router(hooker.router, prefix=BASE_URL)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Reply with the same message
    reply_text = f"You said: {event.message.text}"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

if __name__ == "__main__":
    import asyncio
    import fastapi
    fastapi.run(app, host="0.0.0.0", port=8000)
