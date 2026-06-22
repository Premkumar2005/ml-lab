import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("ToyotaCorolla.csv")

plt.figure(figsize=(8,6))
plt.scatter(data["Age_08_04"], data["Price"], color="blue")

plt.title("Toyota Corolla Dataset")
plt.xlabel("Age of Car (Months)")
plt.ylabel("Price")
plt.grid(True)

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