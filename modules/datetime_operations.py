import datetime
import time

def get_current_datetime():
    current_time = datetime.datetime.now()
    print(f"Current Date and Time: {current_time}")

def calculate_date_difference():
    try:
        date1_str = input("Enter the first date (YYYY-MM-DD): ")
        date2_str = input("Enter the second date (YYYY-MM-DD): ")
        
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        
        difference = abs((date2 - date1).days)
        print(f"Difference: {difference} days")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")

def format_custom_date():
    try:
        date_str = input("Enter a date (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        
        print("Available format codes:")
        print("%Y - Year with century", "%m - Month", "%d - Day")
        print("%A - Weekday name", "%B - Month name")
        
        format_code = input("Enter custom format code: ")
        formatted_date = date.strftime(format_code)
        print(f"Formatted Date: {formatted_date}")
    except ValueError:
        print("Invalid date or format.")

def simple_stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

def countdown_timer():
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        
        for remaining in range(seconds, 0, -1):
            print(f"Time remaining: {remaining} seconds", end='\r')
            time.sleep(1)
        
        print("\nCountdown complete!")
    except ValueError:
        print("Please enter a valid number of seconds.")

def datetime_menu():
    while True:
        print("\n--- Datetime and Time Operations ---")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        
        try:
            selection = int(input("Enter your choice: "))
            
            match selection:
                case 1:
                    get_current_datetime()
                case 2:
                    calculate_date_difference()
                case 3:
                    format_custom_date()
                case 4:
                    simple_stopwatch()
                case 5:
                    countdown_timer()
                case 6:
                    break
                case _:
                    print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")
