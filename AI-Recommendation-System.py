# Import required libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# COURSE DATABASE
courses = {
    "Python Basics":
    "python programming variables loops functions beginner",

    "Machine Learning":
    "python machine learning artificial intelligence regression classification",

    "Artificial Intelligence":
    "python ai neural networks deep learning chatbot",

    "Data Science":
    "python pandas numpy matplotlib statistics visualization",

    "Web Development":
    "html css javascript bootstrap frontend responsive",

    "Java Programming":
    "java object oriented programming oop collections",

    "Cloud Computing":
    "aws azure cloud devops docker kubernetes",

    "Cyber Security":
    "network security ethical hacking penetration testing linux",

    "Database Systems":
    "sql mysql database normalization queries",

    "Mobile App Development":
    "android kotlin java mobile app development"
}

# DISPLAY AVAILABLE COURSES
print("\n========================================")
print("      AI COURSE RECOMMENDATION SYSTEM")
print("========================================\n")
print("Available Courses\n")
for course in courses:
    print("•", course)

# USER INPUT
print("\n----------------------------------------")
print("Enter your interests.")
print("Separate multiple interests using space.")
print("----------------------------------------\n")
user_input = input("Your Interests : ")

# PREPARE DATA
course_names = list(courses.keys())
course_descriptions = list(courses.values())

# CREATE TF-IDF MODEL
vectorizer = TfidfVectorizer()
course_vectors = vectorizer.fit_transform(course_descriptions)

# CONVERT USER INPUT INTO VECTOR
user_vector = vectorizer.transform([user_input])

# CALCULATE COSINE SIMILARITY
similarity_scores = cosine_similarity(user_vector, course_vectors)

# STORE RESULTS
recommendations = []
for i in range(len(course_names)):
    recommendations.append(
        (course_names[i],
         similarity_scores[0][i])
    )

# SORT RESULTS
recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)

# DISPLAY RESULTS
print("\n========================================")
print("      TOP RECOMMENDED COURSES")
print("========================================\n")
rank = 1
for course, score in recommendations:
    print("--------------------------------------")
    print("Rank :", rank)
    print("Course :", course)
    print("Similarity Score :", round(score, 2))
    print("Match Percentage :", round(score * 100, 2), "%")
    rank += 1
print("--------------------------------------")

# BEST RECOMMENDATION
best_course = recommendations[0][0]
best_score = recommendations[0][1]
print("\n========================================")
print("BEST RECOMMENDATION")
print("========================================")
print("Course Name :", best_course)
print("Matching Percentage :", round(best_score * 100,2), "%")
print("\nThank You!")
print("========================================")