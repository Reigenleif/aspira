from fastapi import APIRouter, Depends, Request, HTTPException
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import JoinEvent, MessageEvent, TextMessage, TextSendMessage
import os
from dotenv import load_dotenv
from ..functions.msg_group import msg_group

# Load environment variables
load_dotenv()
CHANNEL_SECRET = os.getenv("CHANNEL_SECRET")
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")

# Initialize LINE Bot API and Webhook Handler
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

router = APIRouter()



# Webhook callback endpoint
@router.post("/callback")
async def callback(request: Request):
    # Get request headers and body
    signature = request.headers.get("X-Line-Signature", "")
    body = await request.body()
    try:
        # Handle webhook body and verify signature
        handler.handle(body.decode("utf-8"), signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    
    
    
@handler.add(JoinEvent)
def handle_join(event: JoinEvent):
    id = event.source.group_id if event.source.group_id else event.source.room_id
    print(f"Bot has joined group/room ID: {id}")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Thank you for inviting me to the group!")
    )