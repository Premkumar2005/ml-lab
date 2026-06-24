import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

plt.figure(figsize=(8, 6))
# Scatter plot of the first two dimensions (Sepal Length vs Sepal Width)
scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', s=50, alpha=0.8)

plt.title('Scatter Plot of Iris Data (Sepal Length vs Sepal Width)')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# Add a legend
handles, _ = scatter.legend_elements()
plt.legend(handles, iris.target_names, title="Classes")

plt.show()





# Hill Climbing Algorithm

def objective_function(x):
    return -(x - 5) ** 2 + 25

def hill_climbing(start):
    current = start

    while True:
        left = current - 1
        right = current + 1

        current_value = objective_function(current)
        left_value = objective_function(left)
        right_value = objective_function(right)

        if left_value > current_value:
            current = left
        elif right_value > current_value:
            current = right
        else:
            break

    return current, objective_function(current)

start = 0
best_x, best_value = hill_climbing(start)

print("Best Solution:", best_x)
print("Maximum Value:", best_value)
