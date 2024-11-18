import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# User data
json_data = {
    "__typename": "User",
    "id": "VXNlcjo0NDE5NjM5Nw==",
    "rest_id": "44196397",
    "affiliates_highlighted_label": {
        "label": {
            "url": {
                "url": "https://twitter.com/X",
                "urlType": "DeepLink"
            },
            "badge": {
                "url": "https://pbs.twimg.com/profile_images/1683899100922511378/5lY42eHs_bigger.jpg"
            },
            "description": "X",
            "userLabelType": "BusinessLabel",
            "userLabelDisplayType": "Badge"
        }
    },
    "is_blue_verified": True,
    "profile_image_shape": "Circle",
    "legacy": {
        "created_at": "Tue Jun 02 20:12:29 +0000 2009",
        "default_profile": False,
        "default_profile_image": False,
        "description": "",
        "entities": {
            "description": {
                "urls": []
            }
        },
        "fast_followers_count": 0,
        "favourites_count": 49058,
        "followers_count": 180333019,
        "friends_count": 573,
        "has_custom_timelines": True,
        "is_translator": False,
        "listed_count": 149572,
        "location": "",
        "media_count": 2144,
        "name": "Elon Musk",
        "normal_followers_count": 180333019,
        "pinned_tweet_ids_str": [
            "1778881361249800203"
        ],
        "possibly_sensitive": False,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/44196397/1690621312",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1683325380441128960/yRsRRjGO_normal.jpg",
        "profile_interstitial_type": "",
        "screen_name": "elonmusk",
        "statuses_count": 42265,
        "translator_type": "none",
        "verified": False,
        "withheld_in_countries": []
    },
    "professional": {
        "rest_id": "1679729435447275522",
        "professional_type": "Creator",
        "category": []
    },
    "legacy_extended_profile": {},
    "is_profile_translatable": False,
    "verification_info": {
        "reason": {
            "description": {
                "text": "This account is verified because it's an affiliate of @X on X. Learn more",
                "entities": [
                    {
                        "from_index": 54,
                        "to_index": 56,
                        "ref": {
                            "url": "https://twitter.com/X",
                            "url_type": "ExternalUrl"
                        }
                    },
                    {
                        "from_index": 63,
                        "to_index": 73,
                        "ref": {
                            "url": "https://help.twitter.com/en/rules-and-policies/profile-labels",
                            "url_type": "ExternalUrl"
                        }
                    }
                ]
            }
        }
    },
    "business_account": {}
}

followers_count = json_data["legacy"]["followers_count"]
favourites_count = json_data["legacy"]["favourites_count"]
# Extract relevant data
followers_count = json_data["legacy"]["followers_count"]
favourites_count = json_data["legacy"]["favourites_count"]
statuses_count = json_data["legacy"]["statuses_count"]
listed_count = json_data["legacy"]["listed_count"]
friends_count = json_data["legacy"]["friends_count"]

# Bar chart: User Metrics
fig, ax = plt.subplots(figsize=(8, 6))
categories = ['Followers', 'Favorites', 'Statuses', 'Listed', 'Friends']
counts = [followers_count, favourites_count, statuses_count, listed_count, friends_count]

ax.bar(categories, counts)
ax.set_xlabel('Metrics')
ax.set_ylabel('Counts')
ax.set_title('User Metrics for Elon Musk')

# Line chart: Followers Over Time
followers_over_time = [100000, 500000, 1000000, 2000000, 5000000]  # Placeholder data
years = ['2017', '2018', '2019', '2020', '2021']

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(years, followers_over_time, marker='o')
ax.set_xlabel('Year')
ax.set_ylabel('Followers')
ax.set_title('Followers Over Time for Elon Musk')

# Scatter plot: Followers vs. Favorites
# Assuming you have another user's data for comparison
other_user_followers = 150000000
other_user_favorites = 70000

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(followers_count, favourites_count, color='blue', label='Elon Musk')
ax.scatter(other_user_followers, other_user_favorites, color='red', label='Other User')
ax.set_xlabel('Followers')
ax.set_ylabel('Favorites')
ax.set_title('Followers vs. Favorites')
ax.legend()

# Heatmap: Correlation Matrix
# Assuming you have additional numeric data to create a correlation matrix
# For example, followers_count, favourites_count, statuses_count, listed_count

data = {
    'Followers': followers_count,
    'Favorites': favourites_count,
    'Statuses': statuses_count,
    'Listed': listed_count
}
correlation_matrix = pd.DataFrame(data, index=['Elon Musk'])

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Correlation Matrix')

plt.show()