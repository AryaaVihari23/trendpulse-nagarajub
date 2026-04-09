import pandas as pd #import pandas library
file_path = "data/trends_20260408.json"
df = pd.read_json(file_path)

print(len(df)) #print total rows

#=================
# step 2 removing duplicates
#=================

df = df.drop_duplicates(subset="post_id")
print("After removing duplicates:", len(df))

# =========================
# Step 3: Remove null values
# =========================
df = df.dropna(subset=["post_id", "title", "score"])
print("After removing nulls:", len(df))

# =========================
# Step 4: Fix data types
# =========================
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# =========================
# Step 5: Remove low scores
# =========================
df = df[df["score"] >= 5]
print("After removing low scores:", len(df))

# =========================
# Step 6: Clean title
# =========================
df["title"] = df["title"].str.strip()

# =========================
# Step 7: Save CSV
# =========================
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

print(f"\nSaved {len(df)} rows to {output_path}")

# =========================
# Step 8: Category summary
# =========================
print("\nStories per category:")
print(df["category"].value_counts())