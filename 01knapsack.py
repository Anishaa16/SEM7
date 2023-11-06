import time

def knapsack(value, weight, capacity):
    n = len(value) - 1
    m = [[-1] * (capacity + 1) for _ in range(n + 1)]

    for w in range(capacity + 1):
        m[0][w] = 0

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weight[i] > w:
                m[i][w] = m[i - 1][w]
            else:
                m[i][w] = max(m[i - 1][w - weight[i]] + value[i], m[i - 1][w])

    # Traceback to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if m[i][w] != m[i - 1][w]:
            selected_items.append(i)
            w -= weight[i]

    return m[n][capacity], selected_items

n = int(input('Enter the number of items: '))
value = input('Enter the values of the {} item(s) in order: '.format(n)).split()
value = [int(v) for v in value]
value.insert(0, None)
weight = input('Enter the positive weights of the {} item(s) in order: '.format(n)).split()
weight = [int(w) for w in weight]
weight.insert(0, None)
capacity = int(input('Enter maximum weight: '))

# Measure execution time
start_time = time.time()
max_value, selected_items = knapsack(value, weight, capacity)
execution_time = time.time() - start_time

# Calculate and display space complexity
space_complexity_bytes = (n + 1) * (capacity + 1) * 8  # Assuming 8 bytes per element in the 2D list
space_complexity_kb = space_complexity_bytes / 1024
space_complexity_mb = space_complexity_kb / 1024

print(f"Space Complexity (estimated): {space_complexity_bytes} bytes, {space_complexity_kb:.2f} KB, {space_complexity_mb:.2f} MB")
print(f"Time Complexity: O({n} * {capacity})")
print(f"Execution Time: {execution_time:.1f} seconds")

print('The maximum value of items that can be carried:', max_value)
print('Selected items:')
for item in selected_items:
    print(f'Item {item}: Weight {weight[item]}, Value {value[item]}')
