import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generate a random password based on the user specifications.
    """
    # Build the pool of available characters
    character_pool = ""
    
    if use_letters:
        character_pool += string.ascii_letters  # Includes both uppercase and lowercase (a-z, A-Z)
    if use_numbers:
        character_pool += string.digits         # Includes numbers (0-9)
    if use_symbols:
        character_pool += string.punctuation    # Includes symbols (!, @, #, $, etc.)
        
    # Guard clause: Check if at least one character type is selected
    if not character_pool:
        return "Error: You must select at least one character type!"

    # Generate a random password by picking characters from the pool
    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("--- 🔐 Welcome to the Python Password Generator 🔐 ---")
    
    # Get password configuration from the user
    try:
        length = int(input("Enter the desired password length (e.g., 12): "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number for the length.")
        return

    # Ask user for preferences (Y/N)
    include_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Generate the password
    generated_password = generate_password(
        length, 
        use_letters=include_letters, 
        use_numbers=include_numbers, 
        use_symbols=include_symbols
    )

    # Display the result
    print("\n--------------------------------")
    print(f"Generated Password: {generated_password}")
    print("--------------------------------")

if __name__ == "__main__":
    main()