# 1. seconds_to_hms(seconds)
def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    return f"{hours:02}:{minutes:02}:{secs:02}"


# 2. celsius_to_fahrenheit(celsius)
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


# 3. split_evenly(total, people)
def split_evenly(total, people):
    each = total // people
    remainder = total % people

    return each, remainder


# 4. initials(full_name)
def initials(full_name):
    words = full_name.split()
    result = ""
    i = 0

    while i < len(words):
        result = result + words[i][0].upper()
        i = i + 1

    return result


# 5. is_palindrome_word(word)
def is_palindrome_word(word):
    word = word.strip().lower()
    return word == word[::-1]


# 6. mask_email(email)
def mask_email(email):
    at = email.index("@")
    name = email[:at]
    domain = email[at:]

    if len(name) <= 2:
        return name[0] + "*" * (len(name) - 1) + domain

    return name[0] + "*" * (len(name) - 2) + name[-1] + domain


# 7. middle(values)
def middle(values):
    n = len(values)

    if n % 2 == 1:
        return values[n // 2]

    return values[n // 2 - 1:n // 2 + 1]


# 8. rotate_left(values, k)
def rotate_left(values, k):
    if len(values) == 0:
        return []

    k = k % len(values)
    return values[k:] + values[:k]


# 9. fib_list(n)
def fib_list(n):
    result = []
    a = 0
    b = 1
    i = 0

    while i < n:
        result.append(a)
        a, b = b, a + b
        i = i + 1

    return result


# 10. collatz_steps(n)
def collatz_steps(n):
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        steps = steps + 1

    return steps


# Examples
print(seconds_to_hms(3661))
print(celsius_to_fahrenheit(25))
print(split_evenly(10, 3))
print(initials("Ahmed Mohamed Ali"))
print(is_palindrome_word("Level"))
print(mask_email("ahmed@gmail.com"))
print(middle([1, 2, 3, 4, 5]))
print(rotate_left([1, 2, 3, 4, 5], 2))
print(fib_list(7))
print(collatz_steps(6))