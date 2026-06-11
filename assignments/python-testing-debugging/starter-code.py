def add(a, b):
    return a - b  # BUG: should add the numbers


def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Fix the bug in add(), then write tests to verify add, is_palindrome, and divide.
