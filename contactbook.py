import json
import os
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    contacts = load_contacts()
    
    name = input("Enter store name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts():
    contacts = load_contacts()
    if contacts:
        for index, contact in enumerate(contacts):
            print(f"Contact {index + 1}:")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print(f"  Address: {contact['address']}")
            print()
    else:
        print("No contacts found.")

def search_contact():
    contacts = load_contacts()
    search_term = input("Enter name or phone number to search: ")
    
    found = False
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            print(f"Found contact:")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print(f"  Address: {contact['address']}")
            print()
            found = True
    
    if not found:
        print("No contacts found with that name or phone number.")

def update_contact():
    contacts = load_contacts()
    
    name = input("Enter the store name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            print("Updating contact:")
            contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ")
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ")
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ")
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    
    print("Contact not found.")

def delete_contact():
    contacts = load_contacts()
    
    name = input("Enter the store name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return
    
    print("Contact not found.")

def main():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()