from twitter.scraper import Scraper
from twitter.util import init_session

def get_twitter_details(username):
    try:
        scraper = Scraper(session=init_session())
        users = scraper.users([username])
        data = users[0]["data"]["user"]["result"]

        # Extract relevant user details
        user_details = {
            'screen_name': data['legacy'].get('screen_name', ''),  # Extracting the username
            'name': data['legacy'].get('name', ''),  # Extracting the name
            'followers_count': data['legacy'].get('followers_count', 0),
            'friends_count': data.get('legacy', {}).get('friends_count', 0),
            'statuses_count': data.get('legacy', {}).get('statuses_count', 0)
            # Add more details as needed
        }

        return user_details
    except KeyError as ke:
        print(f"KeyError occurred while processing the user data: {ke}")
        return None
    except IndexError as ie:
        print(f"IndexError occurred while accessing user data: {ie}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
