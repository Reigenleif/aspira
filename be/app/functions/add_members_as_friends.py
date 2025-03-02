from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("CHANNEL_SECRET")
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN )


def add_members_as_friends(group_names=None):
    """
    Add all members of specified groups or all groups as friends.
    
    Parameters:
        group_names (list or None): Array of group names to add members from.
                                    If None, add members from all groups.
    """
    try:
        # Get all groups (simulate this with an API call if available)
        all_groups = line_bot_api.get_group_summary_list()  # Example method
        group_ids = {
            group['groupName']: group['groupId'] for group in all_groups
        }

        # Determine groups to process
        if group_names is None:
            target_group_ids = group_ids.values()  # All groups
        else:
            target_group_ids = [group_ids[name] for name in group_names if name in group_ids]

        # Iterate over target groups
        for group_id in target_group_ids:
            # Get group members (simulated API call)
            members = line_bot_api.get_group_member_ids(group_id)
            for member_id in members:
                # Send a friend request to each member
                line_bot_api.friend_request(member_id)  # Example method
                print(f"Friend request sent to member ID: {member_id}")

        print("Friend requests processed successfully!")
    except KeyError as e:
        print(f"Error: Group not found. {e}")
    except LineBotApiError as e:
        print(f"Error with LINE API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
