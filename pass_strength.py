import re

def assess_password_strength(password):
    # Initialize score
    score = 0
    feedback = []

    # Initialize counters
    upper_count = len(re.findall(r'[A-Z]', password))
    lower_count = len(re.findall(r'[a-z]', password))
    digit_count = len(re.findall(r'[0-9]', password))
    special_count = len(re.findall(r'[\W_]', password))

    # Criteria 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Criteria 2: Uppercase letters
    if upper_count > 0:
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Criteria 3: Lowercase letters
    if lower_count > 0:
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Criteria 4: Numbers
    if digit_count > 0:
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Criteria 5: Special characters
    if special_count > 0:
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, $).")

    # Provide feedback based on score
    if score == 5:
        strength = "Very Strong"
        feedback = ["Your password is very strong. Well done!"]
    elif score == 4:
        strength = "Strong"
        feedback = ["Your password is strong, but you can improve it by adding more variety."]
    elif score == 3:
        strength = "Medium"
        feedback = ["Your password is okay, but it could be stronger. Consider adding more complexity."]
    else:
        strength = "Weak"
        feedback.append("Your password is weak. Consider making it more complex.")

    return strength, feedback, upper_count, lower_count, digit_count, special_count

def main():
    print("Password Strength Assessment Tool")
    password = input("Enter your password: ")
    
    strength, feedback, upper_count, lower_count, digit_count, special_count = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")
    
    print("\nPassword Analysis:")
    print(f"Uppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")
    print(f"Digits: {digit_count}")
    print(f"Special characters: {special_count}")
    print(f"Total length: {len(password)}")

if __name__ == "__main__":
    main()
