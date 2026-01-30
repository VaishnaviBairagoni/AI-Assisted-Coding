#Task 1: AI-Based Code Completion for Conditional Eligibility Check
def check_voting_eligibility(age, citizenship):
    if age >= 18 and citizenship.lower() == "yes":
        return "Eligible to vote"
    else:
        return "Not eligible to vote"


if __name__ == "__main__":
    age = int(input("Enter age: "))
    citizenship = input("Are you a citizen? (yes/no): ")
    print(check_voting_eligibility(age, citizenship))

#Task 2: AI-Based Code Completion for Loop-Based String Processing
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


if __name__ == "__main__":
    text = input("Enter a string: ")
    v, c = count_vowels_consonants(text)
    print("Vowels:", v)
    print("Consonants:", c)

#Task 3: AI-Assisted Code Completion Reflection Task
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added to library")

    def display_books(self):
        if not self.books:
            print("No books available")
        else:
            print("Available books:")
            for book in self.books:
                print("-", book)


if __name__ == "__main__":
    lib = Library()

    while True:
        print("\n1. Add Book")
        print("2. Display Books")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            book = input("Enter book name: ")
            lib.add_book(book)
        elif choice == 2:
            lib.display_books()
        elif choice == 3:
            print("Exiting system")
            break
        else:
            print("Invalid choice")

#Task 4: AI-Based Code Completion for Class-Based Attendance System
class Attendance:
    def __init__(self):
        self.records = {}

    def mark_attendance(self, name, status):
        self.records[name] = status

    def display_attendance(self):
        for name, status in self.records.items():
            print(name, ":", status)


if __name__ == "__main__":
    att = Attendance()

    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Student name: ")
        status = input("Present/Absent: ")
        att.mark_attendance(name, status)

    print("\nAttendance Record:")
    att.display_attendance()

#Task 5: AI-Based Code Completion for Conditional Menu Navigation
balance = 10000

while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Deposited:", amount)

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid option")

