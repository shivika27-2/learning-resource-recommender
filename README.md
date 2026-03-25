# learning-resource-recommender
# 📚 Personalized Learning Resource Recommender

A machine learning project built as part of the **Fundamentals of AI and ML** course (BYOP Submission).

---

## 📌 Problem Statement

Students often do not know which topics they are weak in and where to find good resources to improve. Teachers also cannot always identify struggling students early enough to help them.

This project solves that by asking a student to enter their scores across 6 topics. The system then automatically detects which topics are weak, classifies the severity of the weakness using a machine learning model, and recommends the best free learning resources for each weak topic.

---

## 💡 Why This Problem Matters

- Students waste time studying topics they already know
- Finding quality resources online is confusing and time-consuming
- Early identification of weak areas leads to better learning outcomes
- This system gives instant, personalized guidance to any student

---

## 🔧 How It Works

```
Student enters name and scores for 6 topics
                ↓
Weak Topic Detection  →  score < 60 is marked as weak
                ↓
Severity Classification  →  Mild / Moderate / Severe
                ↓
Personalized Resource Recommendations printed for each weak topic
```

---

## 🤖 ML Concepts Used

| Concept | How It Is Used |
|---|---|
| Threshold-based Classification | Detects weak topics (score < 60) |
| KMeans Clustering | Groups students into Low / Medium / High performers |
| Random Forest Classifier | Predicts severity of weakness (Mild / Moderate / Severe) |
| Data Generation | Synthetic dataset of 200 students created using NumPy |
| Data Preprocessing | StandardScaler used to normalize scores before clustering |

---

## 📁 Project Structure

```
learning-resource-recommender/
├── main.py                  ← Run this file to start the program
├── requirements.txt         ← All required Python libraries
├── README.md                ← Project documentation
└── src/
    ├── generate_data.py     ← Generates synthetic student score dataset
    ├── weakness_detector.py ← Detects weak topics + KMeans clustering
    └── recommender.py       ← Random Forest model + resource recommendations
```

---

## ⚙️ Setup Instructions

### Requirements
- Python 3.8 or above
- pip (Python package manager)

### Step 1 — Clone the repository
```bash
git clone https://github.com/shivika27-2/learning-resource-recommender.git
cd learning-resource-recommender
```

### Step 2 — Install all dependencies
```bash
pip install -r requirements.txt
```

This installs: `pandas`, `numpy`, `scikit-learn`, `matplotlib`

### Step 3 — Run the program
```bash
python main.py
```

---

## 💻 How to Use

Once you run `python main.py`, the program will ask you to:

1. Enter your name
2. Enter your score (0–100) for each of the 6 topics:
   - Math
   - Statistics
   - Python
   - Linear Algebra
   - ML Basics
   - Data Visualization

The program will then display:
- Your scores with ✓ Good or ⚠ Weak status
- List of weak topics
- Severity level (Mild / Moderate / Severe)
- Recommended free resources for each weak topic

---

## 💻 Sample Output

```
==================================================
  PERSONALIZED LEARNING RESOURCE RECOMMENDER
==================================================

Enter your name: Shivika

Hello Shivika! Please enter your scores for each topic.

  Enter your score for Math (0-100): 45
  Enter your score for Statistics (0-100): 30
  Enter your score for Python (0-100): 72
  Enter your score for Linear_Algebra (0-100): 25
  Enter your score for ML_Basics (0-100): 60
  Enter your score for Data_Visualization (0-100): 80

==================================================
  RESULTS FOR SHIVIKA
==================================================

  Your Scores:
    Math                  45/100   ⚠ Weak
    Statistics            30/100   ⚠ Weak
    Python                72/100   ✓ Good
    Linear_Algebra        25/100   ⚠ Weak
    ML_Basics             60/100   ✓ Good
    Data_Visualization    80/100   ✓ Good

  Weak Topics  : Math, Statistics, Linear_Algebra
  Severity     : Moderate

  Recommended Resources:
  ----------------------------------------

  📘 Math:
      → Khan Academy - Math
        https://www.khanacademy.org/math
      → Math is Fun
        https://www.mathisfun.com

  📘 Statistics:
      → Khan Academy - Statistics
        https://www.khanacademy.org/math/statistics-probability
      → StatQuest (YouTube)
        https://www.youtube.com/@statquest

  📘 Linear_Algebra:
      → 3Blue1Brown - Linear Algebra
        https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
      → MIT OpenCourseWare
        https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/

==================================================
  Good luck with your studies!
==================================================

Check another student? (yes/no): no
```

---

## 📊 Dataset

Since no real student dataset was available, a synthetic dataset of **200 students** was generated using NumPy with realistic score distributions across 6 topics. This is a valid and common approach in ML projects where real data is unavailable or restricted.

The dataset is auto-generated when you run the `src/generate_data.py` file and saved as `data/student_scores.csv`.

---

## 🚧 Challenges Faced

- **No real dataset available** — solved by generating synthetic data with realistic score distributions
- **Class imbalance in severity labels** — some severity levels had fewer samples, affecting classifier accuracy
- **Cold start problem** — the system needs scores as input; it cannot recommend without any data

---

## 🔮 Future Improvements

- Connect to a real student database
- Add a web interface using Flask or Streamlit
- Include more topics and resources
- Track student progress over time

---

## 📦 Dependencies

| Library | Version | Purpose |
|---|---|---|
| pandas | latest | Data handling |
| numpy | latest | Synthetic data generation |
| scikit-learn | latest | KMeans, Random Forest, Scaler |
| matplotlib | latest | Visualizations |

---

## 👤 Author

**Shivika** — Fundamentals of AI and ML, BYOP Submission, 2026
