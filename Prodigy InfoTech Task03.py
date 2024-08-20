import re

def assess_password_strength(password):
    # Define the criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Initialize a score
    score = 0
    feedback = []
    
    # Evaluate the password against the criteria
    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    if uppercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
        
    if lowercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
        
    if number_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one number.")
        
    if special_char_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one special character.")
        
    # Determine the strength based on the score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return strength, feedback

def main():
    password = input("Enter a password to assess: ")
    strength, feedback = assess_password_strength(password)
    
    print(f"Password strength: {strength}")
    
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
