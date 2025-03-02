from linebot import LineBotApi
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def retrieve_all_messages(names=None):
    """
    Retrieve all messages from specific users or all users.

    Parameters:
        names (list or None): A list of LINE display names to filter messages by.
                              If None, retrieve messages from all users.

    Returns:
        dict: A dictionary with display names as keys and their messages as values.
    """
    try:
        # Placeholder for messages storage (simulate API response)
        messages_data = line_bot_api.get_message_history()  # Example method
        user_profiles = line_bot_api.get_user_profile_list()  # Example method

        # Create a map of user IDs to display names
        user_map = {profile.user_id: profile.display_name for profile in user_profiles}

        # Filter messages
        filtered_messages = {}
        for message in messages_data:
            sender_id = message['user_id']
            sender_name = user_map.get(sender_id, "Unknown")

            if names is None or sender_name in names:
                if sender_name not in filtered_messages:
                    filtered_messages[sender_name] = []
                filtered_messages[sender_name].append(message['text'])

        return filtered_messages

    except Exception as e:
        print(f"Error retrieving messages: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Retrieve messages from specific users
    user_messages = retrieve_all_messages(names=["John Doe", "Jane Smith"])
    print(user_messages)

    # Retrieve messages from all users
    all_messages = retrieve_all_messages()
    print(all_messages)