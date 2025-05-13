# Prompt the user to enter their first name
first_name = input("Enter your first name (max 10 characters): ")
while len(first_name) > 10:
    print("First name must be 10 characters or less.")
    first_name = input("Enter your first name (max 10 characters): ")

# Prompt the user to enter their last name
last_name = input("Enter your last name (max 10 characters): ")
while len(last_name) > 10:
    print("Last name must be 10 characters or less.")
    last_name = input("Enter your last name (max 10 characters): ")

# Generate and print the greeting
greeting = f"Hello {first_name} {last_name}!"
print(greeting)