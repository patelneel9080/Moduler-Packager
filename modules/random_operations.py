# modules/random_operations.py
import random
import string

def generate_random_number():
    try:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        count = int(input("Enter number of random numbers to generate: "))
        
        random_numbers = [random.randint(start, end) for _ in range(count)]
        print("Generated Random Numbers:", random_numbers)
    except ValueError:
        print("Please enter valid integers.")

def generate_random_list():
    try:
        length = int(input("Enter length of list: "))
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        
        random_list = random.sample(range(start, end+1), min(length, end-start+1))
        print("Generated Random List:", random_list)
    except ValueError:
        print("Please enter valid integers.")

def create_random_password():
    try:
        length = int(input("Enter password length: "))
        
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation
        
        all_chars = lowercase + uppercase + digits + special_chars
        
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special_chars)
        ]
        
        password.extend(random.choice(all_chars) for _ in range(length - 4))
        
        random.shuffle(password)
        
        password = ''.join(password)
        
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid password length.")

def generate_random_otp():
    """Generate a random One-Time Password (OTP)."""
    try:
        length = int(input("Enter OTP length: "))
        
        otp = ''.join(random.choices(string.digits, k=length))
        print("Generated OTP:", otp)
    except ValueError:
        print("Please enter a valid OTP length.")

def random_sampling():
    """Demonstrate random sampling from a dataset."""
    try:
        dataset = input("Enter comma-separated items (e.g., apple,banana,cherry,date): ").split(',')
        sample_size = int(input("Enter sample size: "))
        
        sample = random.sample(dataset, min(sample_size, len(dataset)))
        print("Random Sample:", sample)
    except ValueError:
        print("Please enter valid inputs.")

def random_menu():
    """Random Data Generation menu."""
    while True:
        print("\n--- Random Data Generation ---")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling")
        print("6. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                generate_random_number()
            elif choice == 2:
                generate_random_list()
            elif choice == 3:
                create_random_password()
            elif choice == 4:
                generate_random_otp()
            elif choice == 5:
                random_sampling()
            elif choice == 6:
                break
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")