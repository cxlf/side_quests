import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
            print("loading...")
            print("program loaded successfully")
    except FileNotFoundError:
        print("an error has occured") 

def add():
    name = input("enter a name to add: ")
    number = input("enter a number: ")
    phone_book[name] = number
    print(f"contact {name} with the number {number} has been added")
    
def remove():
    name = input("enter a name to remove: ")
    if name in phone_book:
        del phone_book[name]
        print(f"{name} has been removed")

def search():
    name = input("enter a name to search: ")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"{name} could not be found")
        
def display():
    if not phone_book:
        print("no data has been added yet")
    else:
        for name, number in phone_book.items():
            print(f"{name}: {number}")
        
def wipe():
    if confirmation():
        phone_book.clear()
        print("all data has been wiped")
    else:
        print("wipe cancelled")
    
def confirmation():
    conf = input("are you sure? (y/n): ")
    if conf == "y":
        return True
    elif conf == "n":
        return False
    
def him():
    img = mpimg.imread("him.png")
    plt.imshow(img)
    plt.show()

def exit():
    save_phone_book()
    print("exiting program...")
    return True

load_phone_book()

while True:
    print("\nmenu")
    print("1. add a contact")
    print("2. remove a contact")
    print("3. search for a contact")
    print("4. display all contacts")
    print("5. wipe all data")
    print("6. him :0000000")
    print("7. exit")
    
    choice = int(input("enter your choice: "))
    
    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        search()
    elif choice == 4:
        display()
    elif choice == 5:
        wipe()
    elif choice == 6:
        him()
    elif choice == 7:
        if exit():
            break
