from linebot import LineBotApi
from linebot.models import TextSendMessage
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("CHANNEL_SECRET")
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def broadcast_message(message, targets=None):
    """
    Broadcast a message to all users or specific users by their display names.

    Parameters:
        message (str): The message to broadcast.
        targets (list or None): An array of LINE display names to broadcast the message to.
                                If None, the message is broadcasted to all users.
    """
    try:
        if targets is None:
            # Broadcast to all users
            line_bot_api.broadcast(TextSendMessage(text=message))
            print("Message broadcasted to all users successfully!")
        else:
            # Retrieve user IDs by display names and send messages
            user_profiles = line_bot_api.get_user_profile_list()  # Example method
            user_map = {profile.display_name: profile.user_id for profile in user_profiles}

            for name in targets:
                user_id = user_map.get(name)
                if user_id:
                    line_bot_api.push_message(user_id, TextSendMessage(text=message))
                    print(f"Message sent to {name} successfully!")
                else:
                    print(f"User with display name '{name}' not found.")

    except Exception as e:
        print(f"Error broadcasting message: {e}")

# Example usage
if __name__ == "__main__":
    # Broadcast message to specific users by display name
    broadcast_message("Hello, this is a targeted message!", targets=["John Doe", "Jane Smith"])