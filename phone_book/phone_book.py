phone_book = {}

def save_phone_book():
    with open("phonebook.txt", "w") as file:
        for name, number in phone_book.items():
            file.write(f"{name}:{number}\n")

def load_phone_book():
    try:
        with open("phonebook.txt", "r") as file:
            for line in file:
                name, number = line.strip().split(":")
                phone_book[name] = number
            print("Program loaded successfully.")
    except FileNotFoundError:
        print("No phonebook file found.")

def add():
    name = input("Enter a name to add: ")
    number = input("Enter a number: ")
    
    if not name or not number:
        print("Name and number cannot be empty.")
        return
    
    if name in phone_book:
        print(f"Contact {name} already exists.")
    else:
        phone_book[name] = number
        save_phone_book()
        print(f"Contact {name} with the number {number} has been added.")

def remove():
    name = input("Enter a name to remove: ")
    if name in phone_book:
        del phone_book[name]
        save_phone_book()
        print(f"{name} has been removed.")
    else:
        print(f"{name} not found in the phonebook.")

def search():
    name = input("Enter a name to search: ")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"{name} not found in the phonebook.")

def display():
    if phone_book:
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")

# ... (previous code)

def exit_program():
    print("Exiting program...")
    save_phone_book()
    return False

# Load the phone book data from a file
load_phone_book()

menu_functions = {
    1: add,
    2: remove,
    3: search,
    4: display,
    5: exit_program
}

while True:
    print("\nMenu")
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. Search for a contact")
    print("4. Display all contacts")
    print("5. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
        if choice in menu_functions:
            if not menu_functions[choice]():  # Check the return value
                break  # Exit the loop if the function returns False
        else:
            print("Invalid choice. Please select a valid option (1-5).")
    except ValueError:
        print("Invalid input. Please enter a number (1-5) to select an option.")
