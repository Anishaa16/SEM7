import time

# Non-Recursive (Iterative) Fibonacci
def fibonacci_non_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Analyze Time Complexity
def analyze_time_complexity(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Analyze Space Complexity
def analyze_space_complexity(func, n):
    import sys
    def get_recursive_depth(n, current_depth=0):
        if n <= 1:
            return current_depth
        return max(
            get_recursive_depth(n - 1, current_depth + 1),
            get_recursive_depth(n - 2, current_depth + 1)
        )

    max_recursion_depth = get_recursive_depth(n)
    space_complexity = max_recursion_depth * sys.getsizeof(sys._getframe())
    return max_recursion_depth, space_complexity

if __name__ == '__main__':
    n = int(input("Enter the value of n for Fibonacci calculation: "))

    non_recursive_result, non_recursive_time = analyze_time_complexity(fibonacci_non_recursive, n)
    max_recursion_depth, space_complexity = analyze_space_complexity(fibonacci_recursive, n)

    print(f"Non-Recursive Fibonacci ({n}): {non_recursive_result}")
    print(f"Non-Recursive Time Complexity: {non_recursive_time} seconds")
    print(f"Maximum Recursion Depth: {max_recursion_depth}")
    print(f"Space Complexity (estimated): {space_complexity} bytes")

    print()

    recursive_result, recursive_time = analyze_time_complexity(fibonacci_recursive, n)
    max_recursion_depth, space_complexity = analyze_space_complexity(fibonacci_recursive, n)

    print(f"Recursive Fibonacci ({n}): {recursive_result}")
    print(f"Recursive Time Complexity: {recursive_time} seconds")
    print(f"Maximum Recursion Depth: {max_recursion_depth}")
    print(f"Space Complexity (estimated): {space_complexity} bytes")
