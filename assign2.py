#Task 1: Refactoring Odd/Even Logic (List Version)
numbers = [10, 15, 20, 25, 30]
odd_sum = 0
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum + num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

#Task 2: Refactoring Odd/Even Logic (Dictionary Version)
numbers = [10, 15, 20, 25, 30]

even_sum = sum(num for num in numbers if num % 2 == 0)
odd_sum = sum(num for num in numbers if num % 2 != 0)

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

#Task 2: Area Calculation Explanation
def calculate_area(shape, value1, value2=0):
    if shape == "circle":
        return 3.14 * value1 * value1
    elif shape == "rectangle":
        return value1 * value2
    elif shape == "triangle":
        return 0.5 * value1 * value2
    else:
        return "Invalid shape"
print(calculate_area("circle", 5))
print(calculate_area("rectangle", 4, 6))
print(calculate_area("triangle", 3, 8))


#Task 3: Prompt Sensitivity Experiment (Cursor AI)
#Prompt-1: “Write a Python program to check whether a number is even or odd.”
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#Prompt-2: “Write optimized Python code with error handling to check even or odd.”
try:
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")
except ValueError:
    print("Invalid input")

#Prompt-3: “Write a reusable Python function to check if a number is even or odd.”
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

