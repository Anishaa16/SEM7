import time

# Function to solve Fractional Knapsack problem using a greedy approach
def fractional_knapsack(values, weights, capacity):
    n = len(values)
    value_per_weight = [(values[i] / weights[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)  # Sort by value per weight in descending order

    max_value = 0.0  # Maximum value to be obtained
    knapsack = [0.0] * n  # Fraction of each item to be taken (initialized to 0)

    for vpw, index in value_per_weight:
        if weights[index] <= capacity:
            max_value += values[index]
            knapsack[index] = 1.0
            capacity -= weights[index]
        else:
            fraction = capacity / weights[index]
            max_value += values[index] * fraction
            knapsack[index] = fraction
            break

    return max_value, knapsack

# Analyze Time Complexity
def analyze_time_complexity(func, values, weights, capacity):
    start_time = time.time()
    result, _ = func(values, weights, capacity)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Analyze Space Complexity
def analyze_space_complexity(values, weights, capacity):
    import sys
    space_complexity = sys.getsizeof(values) + sys.getsizeof(weights) + sys.getsizeof(capacity)
    return space_complexity

if __name__ == '__main__':
    n = int(input("Enter the number of items: "))
    values = list(map(float, input("Enter the values of the items separated by spaces: ").split()))
    weights = list(map(float, input("Enter the weights of the items separated by spaces: ").split()))
    capacity = float(input("Enter the maximum weight capacity of the knapsack: "))

    max_value, knapsack_fraction = fractional_knapsack(values, weights, capacity)

    print(f"The maximum value that can be obtained: {max_value:.2f}")
    print("Item fractions in the knapsack:")
    for i, fraction in enumerate(knapsack_fraction):
        print(f"Item {i+1}: {fraction:.2f}")

    space_complexity = analyze_space_complexity(values, weights, capacity)
    print(f"Space Complexity (estimated): {space_complexity} bytes")

    time_complexity, execution_time = analyze_time_complexity(fractional_knapsack, values, weights, capacity)
    print(f"Time Complexity: O(nlogn) (due to sorting)")
    print(f"Execution Time: {execution_time} seconds")
