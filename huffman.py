import time

class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.huffman = ''

def printNodes(node, val=''):
    newVal = val + str(node.huffman)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.char}   |  {newVal}")

chars = input("Enter Character String:")

# Calculate frequency of characters
dict_frequency = {}
for char in chars:
    if char in dict_frequency:
        dict_frequency[char] += 1
    else:
        dict_frequency[char] = 1

freq = list(dict_frequency.values())

nodes = []

for char, frequency in dict_frequency.items():
    nodes.append(Node(frequency, char))

# Measure execution time
start_time = time.time()

while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda x: x.freq)
    left = nodes[0]
    right = nodes[1]
    left.huffman = 0
    right.huffman = 1
    newNode = Node(left.freq + right.freq, left.char + right.char, left, right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

execution_time = time.time() - start_time

print("Char | Huffman Code")
print("------------------")

# Calculate and display space complexity based on actual data
space_complexity_bytes = len(nodes) * (8 * 2)  # Assuming 8 bytes per Node object and 2 Node objects per entry (left and right)
space_complexity_kb = space_complexity_bytes / 1024
space_complexity_mb = space_complexity_kb / 1024

# Display space complexity and time complexity based on actual data
print(f"Space Complexity (estimated): {space_complexity_bytes} bytes, {space_complexity_kb:.2f} KB, {space_complexity_mb:.2f} MB")
print(f"Time Complexity: O(nlogn) (due to sorting)")

printNodes(nodes[0])
print(f"Execution Time: {execution_time:.5f} seconds")


# Display space complexity and time complexity
#print(f"Space Complexity (estimated): {space_complexity_bytes} bytes, {space_complexity_kb:.2f} KB, {space_complexity_mb:.2f} MB")
#print(f"Time Complexity: O(nlogn) (due to sorting)")


# Display space complexity and time complexity based on actual data
#print(f"Space Complexity (estimated): {space_complexity_bytes} bytes, {space_complexity_kb:.2f} KB, {space_complexity_mb:.2f} MB")
#print(f"Time Complexity: O({len(nodes)} log {len(nodes)}) (due to sorting)")