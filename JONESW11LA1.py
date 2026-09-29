MachineLearning = [
    ("Supervised", "Decision Tree"),
    ("Supervised", "Random Forest"),
    ("Unsupervised", "K-Means"),
    ("Unsupervised", "Gaussian Mixture Model"),
]

for category in ["Supervised", "Unsupervised"]:
    for item in MachineLearning:
        if item[0] == category:
            print(category, ":", item[1])


