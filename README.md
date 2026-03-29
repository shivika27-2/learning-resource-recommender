# 📚 Personalized Learning Resource Recommender

A machine learning project built as part of the **Fundamentals of AI and ML** course (BYOP Submission).  
This system identifies weak topics for students based on their scores and recommends targeted free learning resources.

---

## 📌 Problem Statement

Students often do not know which topics they are weak in and where to find good resources to improve. This project automates that process — the student enters their scores across 6 topics, and the system instantly detects weak areas, classifies severity using ML, and recommends the best free resources for each weak topic.

---

## 💡 Why This Problem Matters

- Students waste time studying topics they already know
- Finding quality resources online is confusing and time-consuming
- Early identification of weak areas leads to better learning outcomes
- Personalized recommendations improve academic performance

---

## 🔧 How It Works

```
Student enters name and scores for 6 topics
                ↓
  [Supervised] Threshold Classification
  Score < 60 = Weak topic detected
                ↓
  [Unsupervised] KMeans Clustering
  Groups student as Low / Medium / High performer
                ↓
  [Supervised] Random Forest Classifier
  Predicts severity → Mild / Moderate / Severe
                ↓
  Personalized Resource Recommendations printed
```

---

## 🤖 AI & ML Concepts Applied (Course Mapping)

| Course Concept | How It Is Used in This Project |
|---|---|
| Supervised Learning | Random Forest Classifier predicts weakness severity |
| Unsupervised Learning | KMeans Clustering groups students by performance |
| Classification | Threshold-based weak topic detection (score < 60) |
| Ensemble Learning | Random Forest uses multiple decision trees |
| Data Preprocessing | StandardScaler normalizes scores before clustering |
| Train / Test Split | 80/20 split used to evaluate the classifier |
| Model Evaluation | Accuracy, Precision, Recall, F1-score reported |
| Feature Importance | Random Forest ranks which topics affect severity most |
| Data Visualization | Bar chart showing weak topic distribution (Matplotlib) |
| Synthetic Data Generation | 200-student dataset created using NumPy |

---

## 📁 Project Structure

```
learning-resource-recommender/
├── main.py                  ← Run this to start the interactive program
├── requirements.txt         ← All required Python libraries
├── README.md                ← Project documentation
└── src/
    ├── generate_data.py     ← Generates synthetic student dataset (200 students, 6 topics)
    ├── weakness_detector.py ← KMeans clustering + weak topic detection + bar chart
    └── recommender.py       ← Random Forest classifier + resource recommendations
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

Installs: `pandas`, `numpy`, `scikit-learn`, `matplotlib`

### Step 3 — Run the interactive program
```bash
python main.py
```

---

## 💻 How to Use

Once you run `python main.py`, the program will:

1. Ask for your **name**
2. Ask you to enter your **score (0–100)** for each of 6 topics:
   - Math
   - Statistics
   - Python
   - Linear Algebra
   - ML Basics
   - Data Visualization
3. Show your scores with ✓ Good or ⚠ Weak status
4. Show weak topics and severity level
5. Print recommended free resources for each weak topic
6. Ask if you want to check another student

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

## 📊 Model Evaluation Results

| Metric | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Train / Test Split | 80% / 20% |
| Overall Accuracy | ~62% |
| Classes | None, Mild, Moderate, Severe |
| Evaluation Method | classification_report (scikit-learn) |

> Note: The dataset is synthetic, so accuracy reflects how well the Random Forest generalizes the severity pattern derived from the threshold rule.

---

## 📊 Dataset Details

| Property | Details |
|---|---|
| Type | Synthetic (generated using NumPy) |
| Number of students | 200 |
| Number of topics | 6 |
| Score range | 20 to 100 |
| Weak threshold | Score below 60 |
| File | data/student_scores.csv (auto-generated) |

> Synthetic data is used because real student data is private and restricted. This is a standard and accepted practice in ML projects.

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| pandas | Data handling and CSV operations |
| numpy | Synthetic data generation |
| scikit-learn | KMeans, Random Forest, StandardScaler, evaluation |
| matplotlib | Data visualization (bar charts) |

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🚧 Challenges Faced

- No real dataset available — solved using synthetic data generation
- Class imbalance in severity labels — fewer samples for Mild and None classes
- Cold start — system needs scores as input to provide recommendations

---

## 🔮 Future Improvements

- Connect to a real student database or LMS
- Build a web interface using Flask or Streamlit
- Add progress tracking over time
- Use SMOTE to handle class imbalance
- Expand resource bank with more topics

---

## 👤 Author

name-Shivika patidar

GitHub: [shivika27-2](https://github.com/shivika27-2)




