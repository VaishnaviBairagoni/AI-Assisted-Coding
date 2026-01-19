#Task 1: Fibonacci Series Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    n = int(input("Enter N: "))
    fibonacci(n)

#Task 2: List Reversal Function
def reverse_list(lst):
    return lst[::-1]


if __name__ == "__main__":
    lst = list(map(int, input("Enter list elements: ").split()))
    print(reverse_list(lst))

#Task 3: String Pattern Matching
def is_valid(s):
    if len(s) == 0:
        return False
    return s[0].isupper() and s.endswith(".")


if __name__ == "__main__":
    s = input("Enter string: ")
    print(is_valid(s))

#Task 4: Email Validator
#Zero-shot Version
def validate_email(email):
    return "@" in email


if __name__ == "__main__":
    email = input("Enter email: ")
    print(validate_email(email))

#Few-shot Version
def validate_email(email):
    if "@" not in email:
        return False

    username, domain = email.split("@", 1)

    if username == "":
        return False

    if "." not in domain:
        return False

    return True


if __name__ == "__main__":
    email = input("Enter email: ")
    print(validate_email(email))

#Task 5: Sum of Digits
#Style-1
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


if __name__ == "__main__":
    n = int(input("Enter number: "))
    print(sum_of_digits(n))

#Style-2
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


if __name__ == "__main__":
    n = int(input("Enter number: "))
    print(sum_of_digits(n))
