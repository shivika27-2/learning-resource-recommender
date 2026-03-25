# ============================================================
# main.py
# Interactive Student Learning Resource Recommender
# Run: python main.py
# ============================================================

# Resource Bank
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
        ("3Blue1Brown - Linear Algebra", "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab"),
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

TOPICS = list(RESOURCES.keys())
WEAK_THRESHOLD = 60


def get_score(topic):
    while True:
        try:
            score = int(input(f"  Enter your score for {topic} (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("  Please enter a number between 0 and 100.")
        except ValueError:
            print("  Invalid input. Please enter a number.")


def get_severity(num_weak):
    if num_weak == 0:   return "None"
    elif num_weak == 1: return "Mild"
    elif num_weak <= 3: return "Moderate"
    else:               return "Severe"


def show_recommendations(weak_topics):
    if not weak_topics:
        print("\n  Great job! No weak topics detected. Keep it up! 🎉")
        return

    print("\n  Recommended Resources:")
    print("  " + "-" * 40)
    for topic in weak_topics:
        print(f"\n  📘 {topic}:")
        for title, url in RESOURCES[topic]:
            print(f"      → {title}")
            print(f"        {url}")


def run():
    print("=" * 50)
    print("  PERSONALIZED LEARNING RESOURCE RECOMMENDER")
    print("=" * 50)

    # Ask for name
    name = input("\nEnter your name: ").strip()
    if not name:
        name = "Student"

    print(f"\nHello {name}! Please enter your scores for each topic.\n")

    # Ask for scores
    scores = {}
    for topic in TOPICS:
        scores[topic] = get_score(topic)

    # Detect weak topics
    weak_topics = [topic for topic in TOPICS if scores[topic] < WEAK_THRESHOLD]
    severity = get_severity(len(weak_topics))

    # Show results
    print("\n" + "=" * 50)
    print(f"  RESULTS FOR {name.upper()}")
    print("=" * 50)

    print("\n  Your Scores:")
    for topic, score in scores.items():
        status = "⚠ Weak" if score < WEAK_THRESHOLD else "✓ Good"
        print(f"    {topic:<20} {score:>3}/100   {status}")

    print(f"\n  Weak Topics  : {', '.join(weak_topics) if weak_topics else 'None'}")
    print(f"  Severity     : {severity}")

    show_recommendations(weak_topics)

    print("\n" + "=" * 50)
    print("  Good luck with your studies!")
    print("=" * 50)

    # Ask if they want to check another student
    again = input("\nCheck another student? (yes/no): ").strip().lower()
    if again in ["yes", "y"]:
        print()
        run()


if __name__ == "__main__":
    run()
    