import json
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from wordcloud import WordCloud
import networkx as nx
import pandas as pd

# Load the data from the 'details.txt' file
with open('Instagram Data/illinoistech_posts.json', 'r') as file:
    data = json.load(file)

# Extract the relevant data
captions = [item['Caption'] for item in data]
likes = [item['Likes'] for item in data]
comments = [item['Comments'] for item in data]
shortcodes = [item['Shortcode'] for item in data]
urls = [item['URL'] for item in data]

# Create a bar chart for likes and comments
fig, ax = plt.subplots(figsize=(12, 6))
x = range(len(likes))
ax.bar(x, likes, label='Likes')
ax.bar([i + 0.2 for i in x], comments, label='Comments')
ax.set_xticks(x)
ax.set_xticklabels(shortcodes)
ax.set_xlabel('Post')
ax.set_ylabel('Count')
ax.set_title('Engagement Analysis')
ax.legend()
plt.xticks(rotation=90)
plt.tight_layout()

# Create a word cloud for the hashtags
hashtags = ' '.join([caption for caption in captions for hashtag in caption.split() if hashtag.startswith('#')])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(hashtags)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Hashtag Analysis')

# Create a network diagram for collaborators
collaborators = set()
for caption in captions:
    for word in caption.split():
        if word.startswith('@'):
            collaborators.add(word[1:])

G = nx.Graph()
G.add_nodes_from(collaborators)
edge_pairs = [(word[1:], word[1:]) for caption in captions for word in caption.split() if word.startswith('@')]
G.add_edges_from(edge_pairs)

pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_size=10)
plt.title('Collaborator Network')

# Create a scatter plot with hover tooltips
df = pd.DataFrame({'Likes': likes, 'Comments': comments, 'Shortcode': shortcodes, 'URL': urls})
fig = go.Figure(data=go.Scatter(
    x=df['Likes'],
    y=df['Comments'],
    mode='markers',
    text=df['Shortcode'],
    hovertemplate='Shortcode: %{text}<br>Likes: %{x}<br>Comments: %{y}'
))
fig.update_layout(
    title='Engagement Scatter Plot',
    xaxis_title='Likes',
    yaxis_title='Comments',
    hovermode='closest'
)
fig.show()

# Create a line plot for engagement over time
df['Date'] = pd.date_range(start='2022-01-01', periods=len(df), freq='D')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['Date'], df['Likes'], label='Likes')
ax.plot(df['Date'], df['Comments'], label='Comments')
ax.set_xlabel('Date')
ax.set_ylabel('Count')
ax.set_title('Engagement Over Time')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()