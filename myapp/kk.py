# Function to display a personalized message
def display_message(name):
    try:
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        message = f"I Miss you too, {name}!"
        return message
    except ValueError as e:
        return str(e)

# Main function
def main():
    print("Welcome to the personalized message program!")
    
    # Asking user for input
    name = input("Enter the name: ")
    
    # Displaying the message
    result = display_message(name)
    print(result)

# Execute the program
if __name__ == "__main__":
    main()
