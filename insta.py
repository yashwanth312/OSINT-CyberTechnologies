import instaloader
import os
import json
from concurrent.futures import ThreadPoolExecutor

def get_instagram_details(username):
    user_details = {}
    post_details = []

    try:
        # Create an Instaloader instance
        L = instaloader.Instaloader()

        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Set the path for the session file
        session_file = os.path.join(script_dir, "instagram_session.json")

        try:
            # Load the session from the session file
            L.load_session_from_file(username, session_file)
        except FileNotFoundError:
            # If the session file doesn't exist, log in and save the session
            L.interactive_login("your_instagram_username_here")
            L.save_session_to_file(session_file)

        # Load the user profile
        profile = instaloader.Profile.from_username(L.context, username)

        user_details = {
            "Username": profile.username,
            "Full Name": profile.full_name,
            "Biography": profile.biography,
            "Followers": profile.followers,
            "Followees": profile.followees,
            "Posts": {
                "Total": profile.mediacount,
            },
            "Private Account": profile.is_private,
            "Business Account": profile.is_business_account,
            "Verified": profile.is_verified,
            "Profile Picture URL": profile.profile_pic_url,
            "Biography Mentions": profile.biography_mentions,
            "External URL": profile.external_url,
            "Followed By": profile.followed_by_viewer,
            "Follows": profile.follows_viewer,
        }

        # Save the user details to a JSON file
        user_json_file = os.path.join(script_dir, "instagram_user_details.json")
        with open(user_json_file, "w") as f:
            json.dump(user_details, f, indent=4)

        # Get the list of follower usernames
        follower_usernames = [follower.username for follower in profile.get_followers()]
        user_details["Follower Usernames"] = follower_usernames

        # Save the follower usernames to a JSON file
        follower_json_file = os.path.join(script_dir, "instagram_follower_usernames.json")
        with open(follower_json_file, "w") as f:
            json.dump(follower_usernames, f, indent=4)

        # Get the list of all posts
        all_posts = [post for post in profile.get_posts()]

        # Use a thread pool to get the post details
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(get_post_details, post) for post in all_posts]
            for future in futures:
                post_details.append(future.result())

        # Save the post details to a JSON file
        post_json_file = os.path.join(script_dir, "instagram_post_details.json")
        with open(post_json_file, "w") as f:
            json.dump(post_details, f, indent=4)

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Instagram profile '{username}' does not exist")

    return user_details, post_details

def get_post_details(post):
    return {
        "Caption": post.caption,
        "Likes": post.likes,
        "Comments": post.comments,
        "Shortcode": post.shortcode,
        "URL": post.url
    }