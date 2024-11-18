# Open Source Intelligence Application

This is a web application built with Flask that allows users to retrieve, view and visualize details from Instagram, Twitter, Reddit and YouTube profiles.

## Project Demo

[![Project Demo](https://img.youtube.com/vi/BHGjZNnLATw/0.jpg)](https://drive.google.com/file/d/1cRBEB3n6ppTSKIEQ_3M9Xd0L8VIFkHD6/view?usp=sharing)


## Features

- **Instagram Details:** Users can input an Instagram username to retrieve details such as username, full name, biography, follower count, following count, total posts, etc. The application also fetches and displays details of the user's recent posts including captions, likes, comments, and post URLs.

- **Twitter Details:** Similar to Instagram, users can input a Twitter username to fetch details such as screen name, real name, follower count, following count, and total tweets.

- **Reddit Details:** Users can input a Reddit username to retrieve details such as username, post karma, comment karma, total posts, total comments, and the list of recent posts and comments.

- **YouTube Details:** Users can input a YouTube username to retrieve details such as channel name, description, country, subscriber count, view count, video count, and the list of recent videos including titles, descriptions, published dates, thumbnails, and video IDs.


## Requirements

- Python >=3.10.10

## Setup
1. **Create a Virtual Environment:**

        # Create a virtual environment (optional but recommended)
        python -m venv osint

        # Activate the virtual environment (Windows)
        venv\Scripts\activate

        # Activate the virtual environment (macOS/Linux)
        source venv/bin/activate

2. **Clone the Repository:**

        git clone https://github.com/your-username/social-media-details.git


3. **Install Dependencies:**

        pip install -r requirements.txt
        
4. **Configuration**
#### Instagram
- Before running the application, make sure to update the Instagram username in the `insta.py` file. Locate the following line in `insta.py`:

        L.interactive_login("your_instagram_username_here")

- Replace it with your Instagram username
#### Reddit

- Similarly update the Reddit `client-id`,`client-secret`, and `user-agent` file. Locate the following line in `redditt.py`:

        reddit = praw.Reddit(client_id='your_client-id',
                     client_secret='your_client_secret',
                     user_agent='your-user-agent')

Here is how to get the `client_id` and `client_secret` needed to authenticate with the Reddit API:

- Create a Reddit account, if you don't already have one.

- Visit the Reddit Apps preferences page by going to this URL: https://www.reddit.com/prefs/apps

- Scroll down to the "Developed Applications" section and click on the "Create App" button.

- Provide the following details for your Reddit app:
        
        Name: Choose a name for your app.
        App type: Select "script".
        Description: Provide a brief description of your app.
        About url: You can leave this blank.
        Redirect uri: http://localhost:8080/
        Click on the "Create app" button.

- After creating the app, Reddit will provide you with the client_id and client_secret for your app. These are the credentials you'll use to authenticate with the Reddit API.

- Use the Credentials in Your Code: Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' in the praw.Reddit() constructor with the values provided by Reddit.

- Set a User Agent: For the user_agent parameter, you need to provide a unique identifier for your application. Ex: 'reddit-user'

#### Youtube
- Also update youtube API key in the `youtubee.py` file. Locate the following line in `youtubee.py`:

        api_key = 'your_youtube_api_key_here'


- Replace it with your own YouTube API key.
Here is how you can get `YouTube API key`
Create a Google Cloud Platform (GCP) Project:

- Go to the Google Cloud Console.
- Create a new project or select an existing one.
- In the Cloud Console, go to the API & Services Dashboard.
- Click on "Enable APIs and Services".
- Search for "YouTube Data API" and click on it.
- Click the "Enable" button.
- In the API & Services Dashboard, navigate to "Credentials" in the left menu.
- Click on "Create Credentials" and select "API key".
- Copy the generated API key.

5. **Run the Application:**

        flask run 

6. **Access the Application:**
Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

1. **Instagram:**
- Enter an Instagram username in the provided input field and click the "Submit" button.
- View the retrieved user details and recent post details.

2. **Twitter:**
- Enter a Twitter username in the provided input field and click the "Submit" button.
- View the retrieved user details.

3. **Reddit:**
- Enter a Reddit username in the provided input field and click the "Submit" button.
- View the retrieved user details and recent post details.

4. **YouTube:**
- Enter a YouTube username in the provided input field and click the "Submit" button.
- View the retrieved channel details and video details.

## Limitations

- While the application does not impose limitations on Instagram search queries, fetching details for users with a large number of followers or posts may result in longer response times. This delay is primarily due to the time taken by Instagram's servers to process and retrieve data for such profiles.


## Screenshots

 **Homepage**

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEj2XWmAG6I6okq2TVU8-TD9C0AUD5mS0h3GGM6FBboOVZ-yy4Pm-8hSvd7cTj31HsHqB-77yoOo2SbMTG8DCPXdJ5-lw7W67drTvjH9mHd_7eDiskVv3VwBQtoUUU1Y6spsvCrn8hiX3wVh2iCHIiGCMT3hhXjTapzRmMEA06WRjCSS080uwE-oCbcA2zKj=s16000)

 **Data Retrieved from Instagram**

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEiXiSbPACvJmusxKuKixTCl2__Bcvg1Nb045nM_qHovC_mS5mhdbsVH9eQzb77rRAyRDtnzbQkXAGQ8CXfHIqagR1y7TybqRG7z-s9nYeN5R28QUw3w7DjXMQHMHpZIc90Pf3pAw1ESSsJtbZ6S7Sv_j1SwFkIL6obGPe-f9zKVdDoa1wPkUUWHtP6l7-y8=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEgCAGFf4Wtc3KM1YIhMT9a6-mHGw25ZQIdWr3pzEGiFPwnv1o64OEJ7e3dhWCwMNNWamhM5MOM1hH3iESPhncGxEUmKGjeGnGLvHQfCAYNKdBs2ZMrx-I_7ponl17V701Y3giwn77UfddJn6Dy7r688096iNGC8hSSaqV3Ie_XCWliT5to_vtgcPv6KYSwQ=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEhGQ68SOPd9SqJgnCkppfpQPimYyfs4z28fyuqTUrYcFfzJ2cO68-UyGP42bCTC_weOxB_myTXp_FQjdulhWrf2WIbkH2dN5Rl_8e-ePpXvl_DklQVZwfeddZtZDCvdq3u07pOPwXMiscmyze-0T4LhmUpyJTJCk28PR6RD8SS10zfP90lWPVPvmF8y8JxJ=s16000)

 **Data Retrieved from Twitter**


![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEh0RMWFNRSEF7faGxxgeok0mECCkDo_xHtjw9HhS7xrUBzAY7s4GSZEFWOdyHeIKLhvsDF4EwLiuW9tyxWQW_hmUNUbykqMn_AGnMq6xXEWFW1MitnRBgfz6WECZABho19jviZQVyGQZgZ2TC3uNevT2Y1qiz8PW3Fd05m9_xWZS0X7fjbC647r5XnuTyX6=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEgzV4WZ_GyXVbZEqsnffmxxQ6vfmoY7nmldTqztTykbnqCHDu9dSGyK9NQcDhPwc1CuxeQbFFpecnQ6_AweH2EGV6zFvBAZaAbWxoahtVU1ceXM8KOe8Z9aq8-6HTQ_TpPooO9DgH85hso0IVybsWN6hfxNcIRNByGxXYHiFZqvib5hcQT6zA2I5xFgWdA2=s16000)

 **Data Retrieved from Reddit**


![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEi_NHewpI1zFq4056L27Vw6AzWBDksDpW_KDXFLSQZG5ybEZNsQESC2oH6kvcIGQfQA1VICokCuqQBPbSCt-lC9lGljy4avJBukKcZRWjfio2xxnlxc4OPtLXVjf4AVHba1nXhEPKHAbbbu_AqJvJcNC5GQsjtQCSphs8NCiCS2fAT290Wkzgod2pObOVXE=s16000)

 **Data Retrieved from YouTube**


![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEhzhnQZaNPdT--eQ_n-HtvfpPQRP8bDkiXFTkX9KmZNXSFqCCwc7iW9gKmvTjyhoOPC4P4LCM83wNPUtni2vifzS3s0u0D1v4toIUC-QMpxBLFfV9pwF1HL0mcVaoo0DosrWmXUQnvuCxUOOlKDY6_gPg6Eq-T8WAchGsPEY8cxEm8vPAxYkuix88T3C3Dl=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEhy2cJuPHCdJMO9PJhvobZXiuqUcWzzq1reVuleJz5qAx61fXqJPDvUwIAHLANpNSEcP57fyCf-fHYEei_BpWcz4BimqA2gWvAyrrriEStFZnE3JVEHm9SgUWVF49-foxMADdhbiXKeGiHJtMGt_jtlK8N_bmXJjzkA1tmPsEmN0JPfwW412VUijZhAOoED=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEhz8mQ-LPZK6wH12sqi5N3Pav-SDsOAfegqkXin4pT5o2pxvZVEhv2JjdWdNTV4erORYybeDXyLyxtOMF2NtkkijTt-HVLXomgGuEwj8jfzCmr_5zJdJkGo6LQjdNvN6n0kxw_btgKVTWVXOwpYJG5aDqtkn_ZnfTTIlCXR_oXec2MyRBMMFaVi5ILgaiOR=s16000)



## Data Visualization

 **Instagram**

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEiMsVaiiSozd9xxQAdtFGXRkGDiD5D9UVdbpk6advV8UvkLs8figkUNN46LxRd7ckU7CiJOPGe_8nMrMXe5x27jn-RtyFyfBxsHYi9SwtuzCqQJxNoJVqFc22RnP1jmJT35bdtZaJoia2HwB88CQ6gDbLjgP1x_VccxPplaQij6fNBTPGFxcWPu_hTVbTgr=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEibzX07ZaqeHAQA33oMORWxrBVP1NHMpibo_42zSkpox9P5-u6ibzqTEOLS2FnnKZXgUTrH4yDOZjT5UUyAOI1E2x0_J3211pGWDdTGWuMLZnM9agEWqZYteeqeb_u7_-W6_aO2scbxwa0Du89BkehbEyi-pQuo16EKea3vayCzHjBWMzRWYZlDJORfhD7g=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEgQYL11twUuN51ulrozVKv3RRmtrAN2P0Y2olxBXoNoiCJEcUuqlueMkDfx9RIc896hr5XwmfSztcY2H6z2lajKxyylGSL8ZM1N4-65rgg3uJRI8P-ncjdAkV3g61811-9J-VNeZQnjjODrQDTbBAkLRP0BdqqIgb208BUKAChyisVKa5X6zaXhzx-4f-Rl=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEgUs18hryUHBlLakdKIFYlqoN8DFyQ5UM8l0TMY1i0dxnLPlBtSvc7DigqJBtyTttgZX3Tw_SUgP05Isqgi8vzNtIdwPwGR0XZVVqCUm1PY8PuTjWG8wRMBUZOrkjagT4l6CE8_NLZ6eyqmdXIrDrItwFhEu9DEz7-pFdcVjyPVDXUnngi3KHK_CZD8Yfoz=s16000)

 **Twitter**


![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEhbzxOtBa9Z02BAi5FfXAUFvxj4aY2YL4ZxLQK2J9SYSloW-CCuqU_SvPyqk1WRn07Okma4mGsClaUhQzRryZHwp_9vqYWfRwmXfz0L1FShLcHa6Zqa7ELRKwr0mtCgXPb9vXWWJ4U_RqR7bBR7JEvgvMo_pQ01g65ESPwkdoTktsPJNl15gELaVceKLOa_=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEgORseXB2K3o9oOnxaHGXWBHt6whJQ9-omanefq84ullm_UN8Ckg0r-dKuWpp5oVAENV6K9PHEAEUz_I28vvdRcq27eVR7Xv5KRAHv33ZJgp_uEYs5at-ONIBRcNu8UIYwlm7bGpxWADmdChQZ6Xb6o3z2fgjkdXqMJwEoewErUMPfKOea6enmswlIfZl09=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEiH72nqKd4U_AzL1Ak_DJ5iT2MS_Jnm4Z2VGspEulno5xSF2aRa4ke6X29IjVgFLrDlSZtWW-uP5dEj9GAURVnk5y41k28SDUE43NfdWJE-GL_ATpde0-iutYVi3HCUAqZ58_ekE5hH9b0m9qA8GKSSDy-eGkXiu-mt5AfMQuVxu0HrPrw-MbsL2J3br1_t=s16000)

 **YouTube**

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEhBB4SCzQzDuFkibzm4Kvo3q28-XZxhCFKYluRMHv6HYglMF7pq2Hc8EF7CSTmRynTRwYrDndIcJ6LWhOcqHUYvQDjSmzFjR-c5U54XMklFBI4ICSjWvN3gz1zeu501LG7BThBURKV4r82AtACigvcXK4jvSOAmCEtrqKy_VRBt5xmAUCRiw05XckE09Sy5=s16000)

## Contributions

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.
