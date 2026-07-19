import datetime 

def show_help():

    print("\nHere's what I can help you with:")
    print("  - Greet me: hello, hi, hey")
    print("  - Ask me:   how are you / what is your name / who created you / what can you do")
    print("  - Utilities: 'date' or 'time' -> shows current date & time")
    print("               'calculate <num1> <+ - * /> <num2>' -> does simple math")
    print("               'help' -> shows this message again")
    print("  - Exit:     bye / exit / quit\n")


def get_current_datetime():

    now = datetime.datetime.now()
    return now.strftime("%A, %d %B %Y | %I:%M:%S %p")


def calculate(user_input):
   
    # Remove the word "calculate" and any extra spaces, then split into parts
    expression = user_input.lower().replace("calculate", "").strip()
    parts = expression.split()

    # We expect exactly 3 parts: number, operator, number (e.g. ["5", "+", "3"])
    if len(parts) != 3:
        return "Please use the format: calculate <number> <operator> <number>\nExample: calculate 5 + 3"

    num1_str, operator, num2_str = parts

    # Validate that both sides are actually numbers
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        return "Both values must be numbers. Example: calculate 10 - 4"

    # Perform the requested operation using if-elif-else
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "I can't divide by zero!"
        result = num1 / num2
    else:
        return f"Unsupported operator '{operator}'. Please use +, -, * or /."

    # Show whole numbers without a trailing ".0" for a cleaner look
    if result == int(result):
        result = int(result)

    return f"The result is: {result}"


# MAIN CHATBOT LOOP

def run_chatbot():
    """Runs the main chatbot loop until the user types an exit command."""

    print("=" * 60)
    print(" Welcome to RuleBot — a simple rule-based chatbot!")
    print("=" * 60)

    # Ask for the user's name once, and remember it for the whole session
    user_name = input("Before we start, what's your name? ").strip().title()
    if user_name == "":
        user_name = "Friend"

    print(f"\nNice to meet you, {user_name}! Type 'help' anytime to see what I can do.\n")

    # The chatbot keeps running until the user says bye/exit/quit
    while True:
        user_input = input(f"{user_name}: ").strip()
        user_input_lower = user_input.lower()

        # Handle empty input
        if user_input_lower == "":
            print("Bot: Please type something so I can help you!")

        # Exit commands
        elif user_input_lower in ["bye", "exit", "quit"]:
            print(f"Bot: Goodbye, {user_name}! It was great chatting with you. 👋")
            break 

        # Greetings 
        elif user_input_lower in ["hello", "hi", "hey"]:
            print(f"Bot: Hello {user_name}! How can I help you today?")

        # Common questions
        elif "how are you" in user_input_lower:
            print("Bot: I'm just a program, so I'm always doing great! How about you?")

        elif "what is your name" in user_input_lower or "your name" in user_input_lower:
            print("Bot: I'm RuleBot, your friendly rule-based chatbot!")

        elif "who created you" in user_input_lower or "who made you" in user_input_lower:
            print(f"Bot: I was created by {user_name} as part of an AI internship project!")

        elif "what can you do" in user_input_lower:
            show_help()

        # Help command
        elif user_input_lower == "help":
            show_help()

        # Date and time
        elif user_input_lower in ["date", "time", "what is the date", "what is the time"]:
            print(f"Bot: Right now it's {get_current_datetime()}")

        # Simple calculator
        elif user_input_lower.startswith("calculate"):
            print(f"Bot: {calculate(user_input)}")


        else:
            print("Bot: Sorry, I didn't understand that. Type 'help' to see what I can do.")

# main entry point
if __name__ == "__main__":
    run_chatbot()
