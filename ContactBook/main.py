# Defining a dictionary to store contacts where the keys are names and values are dictionaries containing contact details.
contacts = {}

# Function to add a new contact to the contact book.
def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    contacts[name] = {'Phone Number': phone_number, 'Email': email, 'Address': address}
    print(f'Contact {name} added successfully.')

# Function to view the list of all contacts.
def view_contacts():
    print("Contact List:")
    for name, details in contacts.items():
        print(f'Name: {name}')
        print(f'Phone Number: {details["Phone Number"]}')
        print(f'Email: {details["Email"]}')
        print(f'Address: {details["Address"]}')
        print('----------------------------------')

# Function to search for a contact by name or phone number.
def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    results = []
    for name, details in contacts.items():
        if search_term in name or search_term in details["Phone Number"]:
            results.append((name, details))
    if results:
        print("Search Results:")
        for name, details in results:
            print(f'Name: {name}')
            print(f'Phone Number: {details["Phone Number"]}')
            print(f'Email: {details["Email"]}')
            print(f'Address: {details["Address"]}')
            print('----------------------------------')
    else:
        print("No matching contacts found.")

# Function to update contact details.
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print(f'Current Details for {name}:')
        print(f'Phone Number: {contacts[name]["Phone Number"]}')
        print(f'Email: {contacts[name]["Email"]}')
        print(f'Address: {contacts[name]["Address"]}')
        choice = input("What do you want to update? (phone/email/address): ").lower()
        if choice == 'phone':
            contacts[name]['Phone Number'] = input("Enter new phone number: ")
        elif choice == 'email':
            contacts[name]['Email'] = input("Enter new email address: ")
        elif choice == 'address':
            contacts[name]['Address'] = input("Enter new address: ")
        else:
            print("Invalid choice.")
        print(f'Contact {name} updated successfully.')
    else:
        print(f'Contact {name} not found.')

# Function to delete a contact.
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f'Contact {name} deleted successfully.')
    else:
        print(f'Contact {name} not found.')

# Main function to provide a user interface for the contact book application.
def main():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thanks for using the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
