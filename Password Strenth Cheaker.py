import re

password = input("Enter your password: ")

strength = 0

# Length check
if len(password) >= 8:
    strength += 1

# Uppercase letter
if re.search(r"[A-Z]", password):
    strength += 1

# Lowercase letter
if re.search(r"[a-z]", password):
    strength += 1

# Number
if re.search(r"[0-9]", password):
    strength += 1

# Special character
if re.search(r"[@$!%*?&#]", password):
    strength += 1

# Result
if strength <= 2:
    print("Password Strength: WEAK ❌")
elif strength == 3 or strength == 4:
    print("Password Strength: MEDIUM ⚠️")
else:
    print("Password Strength: STRONG ✅")
