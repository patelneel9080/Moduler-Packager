import os

def create_new_file():
    """Create a new file."""
    try:
        filename = input("Enter file name: ")
       
        if not filename.endswith('.txt'):
            filename += '.txt'
        
        with open(filename, 'w') as file:
            print(f"File {filename} created successfully!")
    except IOError as e:
        print(f"Error creating file: {e}")

def write_to_file():
    try:
        filename = input("Enter file name: ")
        
        if not filename.endswith('.txt'):
            filename += '.txt'
        
        with open(filename, 'w') as file:
            content = input("Enter data to write: ")
            file.write(content)
            print("Data written successfully!")
    except IOError as e:
        print(f"Error writing to file: {e}")

def read_from_file():
    try:
        filename = input("Enter file name: ")
        
        if not filename.endswith('.txt'):
            filename += '.txt'
        
        with open(filename, 'r') as file:
            content = file.read()
            print("\n--- File Contents ---")
            print(content)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except IOError as e:
        print(f"Error reading file: {e}")

def append_to_file():
    try:
        filename = input("Enter file name: ")
        
        if not filename.endswith('.txt'):
            filename += '.txt'
        
        with open(filename, 'a') as file:
            content = input("Enter data to append: ")
            file.write("\n" + content)
            print("Data appended successfully!")
    except IOError as e:
        print(f"Error appending to file: {e}")

def list_files():
    try:
        print("\n--- Files in Current Directory ---")
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error listing files: {e}")

def file_menu():
    while True:
        print("\n--- File Operations (Custom Module) ---")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. List files in directory")
        print("6. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                create_new_file()
            elif choice == 2:
                write_to_file()
            elif choice == 3:
                read_from_file()
            elif choice == 4:
                append_to_file()
            elif choice == 5:
                list_files()
            elif choice == 6:
                break
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")