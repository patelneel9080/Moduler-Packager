import sys
from modules.datetime_operations import datetime_menu
from modules.math_operations import math_menu
from modules.random_operations import random_menu
from modules.uuid_operations import uuid_menu
from modules.file_operations import file_menu

def primary_menu():
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
            selection = int(input("Enter your choice: "))
            
            match selection:
                case 1:
                    datetime_menu()
                case 2:
                    math_menu()
                case 3:
                    random_menu()
                case 4:
                    uuid_menu()
                case 5:
                    file_menu()
                case 6:
                    explore_module_attributes()
                case 7:
                    print("Thank you for using the Multi-Utility Toolkit!")
                    break
                case _:
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
            selection = int(input("Enter your choice: "))
            
            match selection:
                case 1:
                    print("Attributes in math module:")
                    import math
                    print(dir(math))
                case 2:
                    print("Attributes in random module:")
                    import random
                    print(dir(random))
                case 3:
                    print("Attributes in datetime module:")
                    import datetime
                    print(dir(datetime))
                case 4:
                    break
                case _:
                    print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    primary_menu()
