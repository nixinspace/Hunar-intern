def main():
    print("Welcome to the Greeting Generator!")
    print("Please enter your name details below (each name must be 10 characters or less).")

    # Prompt user for input
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    try:
        if len(first_name) > 10 or len(last_name) > 10:
            print("Error: Each name must be 10 characters or less. Please try again.")
        else:
            # Generate and print greeting
            print(f"Hello {first_name.capitalize()} {last_name.capitalize()}!")
    except ValueError:
        print("Error: Please enter exactly two names separated by a space.")

if __name__ == "__main__":
    main()