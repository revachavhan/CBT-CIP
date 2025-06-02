contacts = {}

def add_contact(name, number):
    key = name.lower().strip()
    if key in contacts:
        overwrite = input(f"Contact '{name}' already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Contact not added.")
            return

    if not number.isdigit() or len(number) < 5 or len(number) > 15:
        print("Invalid number. Please enter digits only (5-15 characters).")
        return

    contacts[key] = (name.strip(), number.strip())
    print(f"Contact {name.strip()} added successfully!")

def delete_contact(name):
    key = name.lower().strip()
    if key in contacts:
        del contacts[key]
        print(f"Contact {name.strip()} deleted successfully!")
    else:
        print("Contact not found.")

def search_contact(name):
    key = name.lower().strip()
    if key in contacts:
        original_name, number = contacts[key]
        print(f"Name: {original_name}, Number: {number}")
    else:
        print("Contact not found.")

def show_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nAll Contacts:")
        for original_name, number in (val for val in contacts.values()):
            print(f"Name: {original_name}, Number: {number}")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Show All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter number: ")
            add_contact(name, number)
        elif choice == '2':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '4':
            show_contacts()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()