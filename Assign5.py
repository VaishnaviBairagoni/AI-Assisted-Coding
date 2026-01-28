#TASK 1: Privacy & Data Security in AI-Generated Code
username = "admin"
password = "1234"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login successful")
else:
    print("Invalid credentials")

#TASK 1: Error Handling in AI-Generated Code
import getpass

stored_username = "admin"
stored_password_hash = "hashed_password_placeholder"

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

if username == stored_username:
    print("Password verification required")
else:
    print("Invalid credentials")


#Task 2: Bias Detection in AI-Generated Decision Systems
def approve_loan(name, gender, income):
    if gender == "male" and income > 30000:
        return "Loan Approved"
    else:
        return "Loan Rejected"

print(approve_loan("Anita", "female", 50000))
print(approve_loan("Rahul", "male", 50000))


#Task 3: Transparency and Explainability in AI-Generated Code
def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

arr = [2, 4, 6, 8, 10]
target = 8

result = binary_search(arr, 0, len(arr) - 1, target)
print("Element found at index:", result)



#Task 4:Ethical Evaluation of AI-Based Scoring Systems
def score_applicant(name, gender, skills, experience, education):
    score = skills * 2 + experience * 3
    if education == "PhD":
        score += 5
    if gender == "male":
        score += 2
    return score

score1 = score_applicant("Anita", "female", 8, 3, "BTech")
score2 = score_applicant("Rahul", "male", 8, 3, "BTech")

print("Score for Anita:", score1)
print("Score for Rahul:", score2)


#Task 5: Inclusiveness and Ethical Variable Design
def process_employee(name, gender):
    if gender == "female":
        print("Assign to HR department")
    else:
        print("Assign to Technical department")

process_employee("Anita", "female")
process_employee("Rahul", "male")
