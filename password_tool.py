def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*()" for char in password):
        score += 1

    if score <= 1:
        return "Weak Password"
    elif score == 2 or score == 3:
        return "Medium Password"
    else:
        return "Strong Password"


# User input
password = input("Enter your password: ")
result = check_password(password)

print("Password Strength:", result)
