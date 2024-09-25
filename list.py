def create_contact():
    name = input("Enter the contact's name:")
    phone = input("Enter the contach's phone number:")
    email = input("Enter the contact's email: ")

    return{
       "name": name,
        "phone":phone,
        "email": email
    }

addressbook = []

def add_contact(contact):
    addressbook.append(contact)
    print(f"{contact["name"]} was added to the address book.")

def view_contact():
    for contact in addressbook:
        print("name:"+ contact["name"]+ ", Phone:" + contact["phone"] + ", Email:" + contact["email"])

def del_contact(name):
    for i, contact in enumerate(addressbook):
        if contact('name') == name:
            del addressbook[i]
            print(f"{name} was removed from the address book")
            return
        print(f"no contact name {name} found.")

while True:
    print("1. Add a contact")
    print("2. View contact")
    print("3. Delete a contact")
    print("4. Quit")
    option = input("Choose an option: ")

    if option == "1":
        contact = create_contact
        add_contact(contact)
    elif option == "2":
        view_contact()
    elif option == "3":
        name = input("Enter the name of the contact to delete: ")
        del_contact(name)
    elif option == "4":
        print("Goodbye")
        break
del_contact()
create_contact()       
add_contact()