import re

# ANSI color codes
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r'[a-z]', password) is None
    uppercase_error = re.search(r'[A-Z]', password) is None
    digit_error = re.search(r'\d', password) is None
    special_char_error = re.search(r'[^A-Za-z0-9]', password) is None

    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    if score == 5:
        return f"{GREEN}Strong 💪{RESET}"
    elif 3 <= score < 5:
        return f"{YELLOW}Moderate ⚠️{RESET}"
    else:
        return f"{RED}Weak ❌{RESET}"

# Example usage
while True:
    pwd = input("Enter a password to check (or type 'exit' to quit): ")
    if pwd.lower() == "exit":
        break
    print("Strength:", check_password_strength(pwd))

