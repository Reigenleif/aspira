from linebot import LineBotApi
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def get_all_friends():
    """
    Retrieve all friends' display names and user IDs, then print them.
    """
    try:
        # Placeholder method: Replace with actual API call to get friend list
        user_profiles = line_bot_api.get_followers_ids() # This method doesn't exist
        user_profiles += line_bot_api.get_ids
        for profile in user_profiles:
            print(f"Display Name: {profile.display_name}, User ID: {profile.user_id}")
    except Exception as e:
        print(f"Error retrieving friends list: {e}")

# Example usage
if __name__ == "__main__":
    get_all_friends()