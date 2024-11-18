from flask import Flask, render_template, request, redirect, url_for
import insta
import twitt
import redditt
import youtubee

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/instagram', methods=['POST'])
def instagram():
    username = request.form['username']
    return redirect(url_for('instagram_details', username=username))

@app.route('/twitter', methods=['POST'])
def twitter():
    username = request.form['username']
    return redirect(url_for('twitter_details', username=username))

@app.route('/reddit', methods=['POST'])
def reddit():
    username = request.form['username']
    return redirect(url_for('reddit_details', username=username))

@app.route('/youtube', methods=['POST'])
def youtube():
    username = request.form['username']
    return redirect(url_for('youtube_details', username=username))

@app.route('/instagram/<username>')
def instagram_details(username):
    user_details, post_details = insta.get_instagram_details(username)
    return render_template('insta_details.html', platform='Instagram', user_details=user_details, post_details=post_details)

@app.route('/twitter/<username>')
def twitter_details(username):
    user_details= twitt.get_twitter_details(username)
    return render_template('twitt_details.html', platform='Twitter', user_details=user_details)

@app.route('/reddit/<username>')
def reddit_details(username):
    user_details, post_details = redditt.get_reddit_details(username)
    return render_template('reddit_details.html', platform='Reddit', user_details=user_details, post_details=post_details)

@app.route('/youtube/<username>')
def youtube_details(username):
    user_details, video_details = youtubee.get_youtube_details(username)
    return render_template('youtube_details.html', platform='YouTube', user_details=user_details, video_details=video_details)


if __name__ == '__main__':
    app.run(debug=True)