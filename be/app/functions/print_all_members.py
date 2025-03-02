from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def display_group_members_profiles():
    """
    Retrieve and display the profiles of members from all groups.
    """
    try:
        # Get all groups (simulate this with an API call if available)
        all_groups = line_bot_api.get_group_summary()  # Example method
        
        for group in all_groups:
            group_id = group['groupId']
            group_name = group['groupName']
            print(f"\nGroup: {group_name} (ID: {group_id})")
            
            # Get group members (simulated API call)
            members = line_bot_api.get_group_member_ids(group_id)
            for member_id in members:
                # Get member profile (simulated API call)
                profile = line_bot_api.get_profile(member_id)
                print(f"Display Name: {profile.display_name}, User ID: {profile.user_id}")
    
    except LineBotApiError as e:
        print(f"Error with LINE API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    display_group_members_profiles()