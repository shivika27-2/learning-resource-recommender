# ============================================================
# generate_data.py
# Step 1: Create synthetic student score data
# Run this first to generate data/student_scores.csv
# ============================================================

import pandas as pd
import numpy as np
import os

# Set seed so results are the same every time you run
np.random.seed(42)

# ----- Settings -----
NUM_STUDENTS = 200
TOPICS = ["Math", "Statistics", "Python", "Linear_Algebra", "ML_Basics", "Data_Visualization"]

# ----- Generate Data -----
data = {"Student_ID": [f"S{str(i+1).zfill(3)}" for i in range(NUM_STUDENTS)]}

for topic in TOPICS:
    # Scores between 20 and 100, with some students struggling (realistic spread)
    scores = np.random.randint(20, 101, size=NUM_STUDENTS)
    data[topic] = scores

df = pd.DataFrame(data)

# Save to CSV
os.makedirs("data", exist_ok=True)
df.to_csv("data/student_scores.csv", index=False)

print("✅ student_scores.csv created with", NUM_STUDENTS, "students!")
print(df.head())