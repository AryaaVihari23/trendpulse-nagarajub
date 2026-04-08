#import required libraries

import requests   #to call Apis
import json       #to save data into json file
import time       #to add delay
import os         #to create folder
from datetime import datetime   #to get current date & time

#step1 define api urls
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Header (good practice to identify our app)
headers = {"User-Agent": "TrendPulse/1.0"}


# Step 2: Define categories and keywords
# We will match these keywords with story titles
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# Step 3: Fetch top 500 story IDs
try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    story_ids = response.json()[:500]   # take only first 500
    print("Fetched top story IDs successfully")
except Exception as e:
    print("Error fetching top stories:", e)
    story_ids = []

# Step 4: Create empty list to store final data
collected_stories = []


# Step 5: Loop through each category
for category, keywords in categories.items():

    print(f"\nProcessing category: {category}")
    count = 0   # to limit 25 stories per category

    # Step 6: Loop through story IDs
    for story_id in story_ids:

        # Stop when we reach 25 stories for this category
        if count >= 25:
            break

        # Step 7: Fetch each story details
        try:
            url = ITEM_URL.format(story_id)
            res = requests.get(url, headers=headers)
            story = res.json()
        except:
            print(f"Failed to fetch story {story_id}")
            continue   # skip this story and move next

        # Step 8: Check if story is valid
        if not story or "title" not in story:
            continue

        # Step 9: Convert title to lowercase for matching
        title = story["title"].lower()

        # Step 10: Check if any keyword matches
        # Example: if "ai" in title → category = technology
        if any(keyword in title for keyword in keywords):

            # Step 11: Extract required fields
            data = {
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "unknown"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Step 12: Add to list
            collected_stories.append(data)
            count += 1

    # Step 13: Wait 2 seconds after each category
    print(f"Collected {count} stories for {category}")
    time.sleep(2)


# Step 14: Create "data" folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")


# Step 15: Create file name with current date
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"


# Step 16: Save data into JSON file
with open(filename, "w") as f:
    json.dump(collected_stories, f, indent=4)


# Step 17: Final output message
print(f"\nCollected {len(collected_stories)} stories. Saved to {filename}")