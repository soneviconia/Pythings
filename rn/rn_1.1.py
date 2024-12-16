import random
from termcolor import colored

def generate_random_number():
    try:
        user_input = input(colored("Enter the maximum number: ", "blue", attrs=["bold"]))
        
        if not user_input.isdigit():
            raise ValueError("Invalid input! Please enter a valid positive number.")
        
        maxnum = int(user_input)
        
        if maxnum <= 0:
            raise ValueError("Please enter a number greater than 0.")
        
        rannum = random.randint(0, maxnum)
        
        print("\n" + colored("Random Number Generator", "yellow", attrs=["bold", "underline"]))
        print(colored("-" * 40, "cyan"))
        print(colored("Max:", "red"), colored(maxnum, "light_red"))
        print(colored("Number:", "green"), colored(rannum, "light_green"))
        print(colored("-" * 40, "cyan")) 
    
    except ValueError as e:
        print(colored(f"Error: {e}", "red"))
generate_random_number()
