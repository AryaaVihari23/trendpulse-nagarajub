# Import libraries
import pandas as pd
import numpy as np

# =========================
# Step 1: Load and Explore
# =========================

# Load cleaned CSV from Task 2
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

# Print shape (rows, columns)
print("Loaded data:", df.shape)

# Print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Calculate averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score   :", avg_score)
print("Average comments:", avg_comments)

# =========================
# Step 2: NumPy Analysis
# =========================

scores = df["score"].values  # convert to NumPy array

print("\n--- NumPy Stats ---")

# Mean, Median, Standard Deviation
print("Mean score   :", np.mean(scores))
print("Median score :", np.median(scores))
print("Std deviation:", np.std(scores))

# Max and Min
print("Max score    :", np.max(scores))
print("Min score    :", np.min(scores))

# Category with most stories
category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# Story with most comments
max_comments_row = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:")
print(max_comments_row["title"], "—", max_comments_row["num_comments"], "comments")

# =========================
# Step 3: Add New Columns
# =========================

# Engagement = comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular = score > average score
df["is_popular"] = df["score"] > avg_score

# =========================
# Step 4: Save Result
# =========================

output_path = "data/trends_analysed.csv"
df.to_csv(output_path, index=False)

print(f"\nSaved to {output_path}")