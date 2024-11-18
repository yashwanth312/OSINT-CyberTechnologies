import praw
import os
import json
from concurrent.futures import ThreadPoolExecutor

def get_reddit_details(username):
    user_details = {}
    post_details = []

    try:
        # Create a Reddit instance
        reddit = praw.Reddit(client_id='your_client-id',
               client_secret='your_client_secret',
               user_agent='your-user-agent')

        # Get the Redditor object
        redditor = reddit.redditor(username)

        user_details = {
            "Username": redditor.name,
            "Total Karma": redditor.link_karma + redditor.comment_karma,
            "Link Karma": redditor.link_karma,
            "Comment Karma": redditor.comment_karma,
            "Is Gold": redditor.is_gold,
            "Is Mod": redditor.is_mod,
            "Verified Email": redditor.has_verified_email,
            "Created UTC": redditor.created_utc
        }

        # Save the user details to a JSON file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        user_json_file = os.path.join(script_dir, "reddit_user_details.json")
        with open(user_json_file, "w") as f:
            json.dump(user_details, f, indent=4)

        # Get the list of posts
        posts = list(redditor.submissions.new(limit=None))

        # Use a thread pool to get the post details
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(get_post_details, post) for post in posts]
            for future in futures:
                post_details.append(future.result())

        # Save the post details to a JSON file
        post_json_file = os.path.join(script_dir, "reddit_post_details.json")
        with open(post_json_file, "w") as f:
            json.dump(post_details, f, indent=4)

    except Exception as e:
        print("An error occurred:", e)

    return user_details, post_details

def get_post_details(post):
    return {
        "Title": post.title,
        "Score": post.score,
        "Num Comments": post.num_comments,
        "URL": post.url
    }
