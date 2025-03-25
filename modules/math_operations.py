import math

def calculate_factorial():
    try:
        num = int(input("Enter a number: "))
        result = math.factorial(num)
        print(f"Factorial of {num}: {result}")
    except ValueError:
        print("Please enter a valid integer.")

def solve_compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): ")) / 100
        time = float(input("Enter time (in years): "))
        
        compound_interest = principal * (1 + rate) ** time - principal
        print(f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        print("Please enter valid numbers.")

def trigonometric_calculations():
    try:
        angle = float(input("Enter angle in degrees: "))
        rad_angle = math.radians(angle)
        
        print(f"Sine of {angle} degrees: {math.sin(rad_angle):.4f}")
        print(f"Cosine of {angle} degrees: {math.cos(rad_angle):.4f}")
        print(f"Tangent of {angle} degrees: {math.tan(rad_angle):.4f}")
    except ValueError:
        print("Please enter a valid number.")

def calculate_geometric_shapes():
    print("\nGeometric Shapes:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    
    try:
        selection = int(input("Enter your choice: "))
        
        match selection:
            case 1:
                radius = float(input("Enter radius: "))
                area = math.pi * radius ** 2
                print(f"Area of Circle: {area:.2f}")
            case 2:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = length * width
                print(f"Area of Rectangle: {area:.2f}")
            case 3:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = 0.5 * base * height
                print(f"Area of Triangle: {area:.2f}")
            case _:
                print("Invalid choice.")
    except ValueError:
        print("Please enter valid numbers.")

def math_menu():
    while True:
        print("\n--- Mathematical Operations ---")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        
        try:
            selection = int(input("Enter your choice: "))
            
            match selection:
                case 1:
                    calculate_factorial()
                case 2:
                    solve_compound_interest()
                case 3:
                    trigonometric_calculations()
                case 4:
                    calculate_geometric_shapes()
                case 5:
                    break
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
            
