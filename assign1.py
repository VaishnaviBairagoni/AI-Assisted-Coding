#Task 1: AI-Generated Logic Without Modularization (Fibonacci Sequence Without Functions)
#fibonaccci series up to n terms
# Accept user input

n = int(input("Enter the number of terms: "))

# Initialize first two terms
a = 0
b = 1

# Handle edge cases
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

#Task 2: AI Code Optimization & Cleanup (Improving Efficiency)
n = int(input("Enter the number of terms: "))

prev, curr = 0, 1

for i in range(n):
    print(prev, end=" ")
    prev, curr = curr, prev + curr

#Task 3: Modular Design Using AI Assistance (Fibonacci Using Functions)
# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = []
    prev, curr = 0, 1

    for i in range(n):
        sequence.append(prev)
        prev, curr = curr, prev + curr

    return sequence


# Take user input
n = int(input("Enter the number of terms: "))

# Call the function and print the result
result = fibonacci(n)
print("Fibonacci sequence:", result)


#Task 5: AI-Generated Iterative vs Recursive Fibonacci Approaches (DifferentAlgorithmic Approaches for Fibonacci Series)
# Iterative approach
def fibonacci_iterative(n):
    prev, curr = 0, 1
    result = []

    for i in range(n):
        result.append(prev)
        prev, curr = curr, prev + curr

    return result


# User input
n = int(input("Enter number of terms: "))
print("Iterative Fibonacci:", fibonacci_iterative(n))


# Recursive approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# User input
n = int(input("Enter number of terms: "))

print("Recursive Fibonacci:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

