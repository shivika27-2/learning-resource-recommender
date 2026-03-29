# ============================================================
# recommender.py
# Step 3: Recommend learning resources based on weak topics
# Classifies severity (Mild / Moderate / Severe) using ML
# Then maps weak topics → curated resource links
# ============================================================

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import os

# ----- Resource Bank -----
# Topic → list of [Title, URL]
RESOURCES = {
    "Math": [
        ("Khan Academy - Math", "https://www.khanacademy.org/math"),
        ("Math is Fun", "https://www.mathisfun.com"),
    ],
    "Statistics": [
        ("Khan Academy - Statistics", "https://www.khanacademy.org/math/statistics-probability"),
        ("StatQuest (YouTube)", "https://www.youtube.com/@statquest"),
    ],
    "Python": [
        ("Python Official Docs", "https://docs.python.org/3/tutorial/"),
        ("W3Schools Python", "https://www.w3schools.com/python/"),
    ],
    "Linear_Algebra": [
        ("3Blue1Brown - Essence of Linear Algebra", "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab"),
        ("MIT OpenCourseWare", "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"),
    ],
    "ML_Basics": [
        ("Google ML Crash Course", "https://developers.google.com/machine-learning/crash-course"),
        ("Scikit-learn Docs", "https://scikit-learn.org/stable/getting_started.html"),
    ],
    "Data_Visualization": [
        ("Matplotlib Tutorial", "https://matplotlib.org/stable/tutorials/index.html"),
        ("Seaborn Gallery", "https://seaborn.pydata.org/examples/index.html"),
    ],
}

# ----- Load Weakness Report -----
df = pd.read_csv("outputs/student_weakness_report.csv")
topics = ["Math", "Statistics", "Python", "Linear_Algebra", "ML_Basics", "Data_Visualization"]

# ----- Severity Classification Using ML -----
# Label: 0 = No Weakness, 1 = Mild, 2 = Moderate, 3 = Severe
def classify_severity(num_weak):
    if num_weak == 0:   return "None"
    elif num_weak == 1: return "Mild"
    elif num_weak <= 3: return "Moderate"
    else:               return "Severe"

df["Severity"] = df["Num_Weak"].apply(classify_severity)

# Train a simple Random Forest to predict severity from scores
X = df[topics]
y = df["Severity"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("=" * 50)
print("SEVERITY CLASSIFICATION REPORT")
print("=" * 50)
print(classification_report(y_test, y_pred, zero_division=0))

# Attach ML-predicted severity to full dataframe
df["Predicted_Severity"] = model.predict(X)

# ----- Generate Recommendations -----
def recommend(row):
    weak_topics_raw = row["Weak_Topics"]

    # Parse string list back to actual list
    if isinstance(weak_topics_raw, str):
        weak_topics_raw = weak_topics_raw.strip("[]").replace("'", "").split(", ")

    if weak_topics_raw == ["None"]:
        return "Great job! No weak topics detected. Keep it up! 🎉"

    lines = []
    for topic in weak_topics_raw:
        topic = topic.strip()
        if topic in RESOURCES:
            lines.append(f"  📘 {topic}:")
            for title, url in RESOURCES[topic]:
                lines.append(f"      → {title}: {url}")
    return "\n".join(lines) if lines else "No resources found."

df["Recommendations"] = df.apply(recommend, axis=1)

# ----- Save Final Output -----
df.to_csv("outputs/final_recommendations.csv", index=False)

# ----- Print Sample Output -----
print("\n" + "=" * 50)
print("SAMPLE RECOMMENDATIONS (First 5 Students)")
print("=" * 50)
for _, row in df.head(5).iterrows():
    print(f"\nStudent: {row['Student_ID']} | Severity: {row['Predicted_Severity']}")
    print(f"Weak Topics: {row['Weak_Topics']}")
    print("Resources:")
    print(row["Recommendations"])
    print("-" * 40)

print("\n✅ Full recommendations saved to outputs/final_recommendations.csv")
# Feature Importance Chart
importances = model.feature_importances_
plt.figure(figsize=(8, 5))
plt.barh(topics, importances, color="steelblue", edgecolor="black")
plt.title("Feature Importance - Which topics affect severity most?")
plt.xlabel("Importance Score")
plt.tight_layout()
plt.savefig("outputs/feature_importance.png", dpi=150)
print("📊 Feature importance chart saved!")

# Confusion Matrix
from sklearn.metrics import ConfusionMatrixDisplay
plt.figure(figsize=(7, 5))
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Confusion Matrix - Severity Prediction")
plt.tight_layout()
plt.savefig("outputs/confusion_matrix.png", dpi=150)
print("📊 Confusion matrix saved!")