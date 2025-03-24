import sys
from modules.datetime_operations import datetime_menu
from modules.math_operations import math_menu
from modules.random_operations import random_menu
from modules.uuid_operations import uuid_menu
from modules.file_operations import file_menu

def main_menu():
    while True:
        print("\n--- Multi-Utility Toolkit ---")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                datetime_menu()
            elif choice == 2:
                math_menu()
            elif choice == 3:
                random_menu()
            elif choice == 4:
                uuid_menu()
            elif choice == 5:
                file_menu()
            elif choice == 6:
                explore_module_attributes()
            elif choice == 7:
                print("Thank you for using the Multi-Utility Toolkit!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")

def explore_module_attributes():
    while True:
        print("\n--- Explore Module Attributes ---")
        print("1. Explore math module")
        print("2. Explore random module")
        print("3. Explore datetime module")
        print("4. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                print("Attributes in math module:")
                import math
                print(dir(math))
            elif choice == 2:
                print("Attributes in random module:")
                import random
                print(dir(random))
            elif choice == 3:
                print("Attributes in datetime module:")
                import datetime
                print(dir(datetime))
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main_menu()
