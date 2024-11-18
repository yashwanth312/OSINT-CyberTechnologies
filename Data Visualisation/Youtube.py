import json
import matplotlib.pyplot as plt

with open("youtube.txt", "r") as file:
    data = json.load(file)

num_videos = len(data)
print("Number of videos:", num_videos)

published_dates = []
for video in data:
    if "Published At" in video:
        published_dates.append(video["Published At"])

year_counts = {}
for date in published_dates:
    year = date[:4]
    year_counts[year] = year_counts.get(year, 0) + 1

years = list(year_counts.keys())
counts = list(year_counts.values())

# Increase the width of the figure
plt.figure(figsize=(10, 6))

plt.bar(years, counts)
plt.xlabel("Year")
plt.ylabel("Number of Videos")
plt.title("Number of Videos Published per Year")
plt.show()