import os
import json
from googleapiclient.discovery import build
from concurrent.futures import ThreadPoolExecutor

def fetch_videos(youtube, playlist_id, next_page_token=None):
    all_videos = []

    try:
        playlist_items_response = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        videos = playlist_items_response.get('items', [])
        all_videos.extend([get_video_details(video) for video in videos])

        next_page_token = playlist_items_response.get('nextPageToken')

        if next_page_token:
            all_videos.extend(fetch_videos(youtube, playlist_id, next_page_token))
    except Exception as e:
        print("An error occurred while fetching videos:", e)

    return all_videos

def get_youtube_details(username):
    user_details = {}
    video_details = []

    try:
        # Set up the YouTube API service
        api_key = 'your_youtube_api_key_here'
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Get the channel details
        channel_response = youtube.channels().list(
            part='snippet,statistics',
            forUsername=username
        ).execute()

        if channel_response['items']:
            channel = channel_response['items'][0]['snippet']
            user_details = {
                "Username": channel.get('title', ''),
                "Description": channel.get('description', ''),
                "Country": channel.get('country', ''),
            }

            # Get statistics data
            statistics = channel_response['items'][0]['statistics']
            user_details.update({
                "Subscriber Count": statistics.get('subscriberCount', ''),
                "View Count": statistics.get('viewCount', ''),
                "Video Count": statistics.get('videoCount', ''),
            })

            # Get the list of videos
            playlist_response = youtube.channels().list(
                part='contentDetails',
                forUsername=username
            ).execute()
            uploads_playlist_id = playlist_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

            video_details = fetch_videos(youtube, uploads_playlist_id)

    except Exception as e:
        print("An error occurred:", e)

    return user_details, video_details

def get_video_details(video):
    return {
        "Title": video['snippet']['title'],
        "Description": video['snippet']['description'],
        "Published At": video['snippet']['publishedAt'],
        "Thumbnail": video['snippet']['thumbnails']['default']['url'],  # Use default quality thumbnail
        "Video ID": video['snippet']['resourceId']['videoId']
    }
