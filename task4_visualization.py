# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# Step 1: Load Data & Setup
# =========================

# Load analysed CSV
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

# Create outputs folder if not exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# =========================
# Chart 1: Top 10 Stories by Score
# =========================

# Get top 10 stories
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles (max 50 chars)
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure(figsize=(10, 6))
plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()

# Save chart
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# =========================
# Chart 2: Stories per Category
# =========================

category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

# Save chart
plt.savefig("outputs/chart2_categories.png")
plt.close()

# =========================
# Chart 3: Score vs Comments
# =========================

plt.figure(figsize=(8, 5))

# Separate popular and non-popular
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

# Scatter plot
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

# Save chart
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# =========================
# Bonus: Dashboard
# =========================

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1 in dashboard
axes[0].barh(top10["short_title"], top10["score"])
axes[0].set_title("Top 10 Stories")
axes[0].invert_yaxis()

# Chart 2 in dashboard
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Stories per Category")

# Chart 3 in dashboard
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

# Overall title
plt.suptitle("TrendPulse Dashboard")

# Save dashboard
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in outputs/ folder")