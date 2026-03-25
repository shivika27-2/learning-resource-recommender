# ============================================================
# weakness_detector.py
# Step 2: Detect weak topics for each student
# Uses a simple threshold (score < 60 = weak)
# Also uses KMeans clustering to group students
# ============================================================

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os

# ----- Load Data -----
df = pd.read_csv("data/student_scores.csv")
topics = ["Math", "Statistics", "Python", "Linear_Algebra", "ML_Basics", "Data_Visualization"]

print("=" * 50)
print("STUDENT SCORE SUMMARY")
print("=" * 50)
print(df[topics].describe().round(1))

# ----- Method 1: Threshold-Based Weak Detection -----
# A topic is "weak" if score < 60
WEAK_THRESHOLD = 60

def get_weak_topics(row):
    weak = [topic for topic in topics if row[topic] < WEAK_THRESHOLD]
    return weak if weak else ["None"]

df["Weak_Topics"] = df.apply(get_weak_topics, axis=1)
df["Num_Weak"] = df["Weak_Topics"].apply(lambda x: 0 if x == ["None"] else len(x))

# ----- Method 2: KMeans Clustering -----
# Group students into 3 clusters: Low / Medium / High performers
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[topics])

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Label clusters by average score
cluster_avg = df.groupby("Cluster")[topics].mean().mean(axis=1)
sorted_clusters = cluster_avg.sort_values().index.tolist()
label_map = {sorted_clusters[0]: "Low", sorted_clusters[1]: "Medium", sorted_clusters[2]: "High"}
df["Performance_Group"] = df["Cluster"].map(label_map)

# ----- Save Results -----
os.makedirs("outputs", exist_ok=True)
df.to_csv("outputs/student_weakness_report.csv", index=False)

print("\n✅ Weak topic detection complete!")
print(df[["Student_ID", "Weak_Topics", "Num_Weak", "Performance_Group"]].head(10).to_string())

# ----- Plot: How many students are weak in each topic? -----
weak_counts = {topic: (df[topic] < WEAK_THRESHOLD).sum() for topic in topics}

plt.figure(figsize=(8, 5))
plt.bar(weak_counts.keys(), weak_counts.values(), color="salmon", edgecolor="black")
plt.title("Number of Students Weak in Each Topic (Score < 60)", fontsize=13)
plt.xlabel("Topic")
plt.ylabel("Number of Students")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("outputs/weak_topic_chart.png", dpi=150)
plt.close()
print("\n📊 Chart saved to outputs/weak_topic_chart.png")