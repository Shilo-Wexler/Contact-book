import json
def show_menu()->None:
    open_menu=  "* "*19
    option1 = "*  Enter 1 to Viewing contacts "
    option2 = "*  Enter 2 to Adding a new contact"
    option3 = "*  Enter 2 Contact search "
    option4 = "*  Enter 4 to Delete contact"
    option5 = "*  Enter 'quit' to To exit "
    print(open_menu)
    print(option1, " " * (34-len(option1)),"*")
    print(option2," " * (30-len(option2)),"*" )
    print(option3, " " * (34 - len(option3)),"*")
    print(option4, " " * (34 - len(option4)),"*")
    print(option5, " " * (34 - len(option5)),"*")
    print(open_menu)
def save_contact(contact):
    try:
        with open("contacts.json", "r") as f:
            book = json.load(f)
            book.append(contact)
        with open("contacts.json" , "w") as f:
            json.dump(book, f, indent= 2)
    except FileNotFoundError:
        with open("contacts.json" , "w") as f:
            json.dump([contact], f, indent= 2)
def add_contact()->dict:
    contact_name = input("Enter the contact name: ")
    contact_num = input("Enter the contact phone number: ")
    new_contact = {contact_name: contact_num}
    save_contact(new_contact)
    return new_contact
def pretty_print(contact_book:list[dict]|dict)->None:
    if type(contact_book) == list:
        for person in contact_book:
            for name, phone in person.items():
                print(f"Name: {name}, Phone number: {phone}")
    elif type(contact_book) == dict:
        for name, phone in contact_book.items():
            print(f"Name: {name}, Phone number: {phone}")
def show_contacts()->list[dict]|None:
    try:
        with open("contacts.json", "r") as f:
            book = json.load(f)
            print(f'You have {len(book)} contacts')
            pretty_print(book)
            return book
    except FileNotFoundError:
        print("You don't have any contacts yet. ")
        return None
def menu_selection(user_select:str)->None:
    if user_select == '1':
        show_contacts()
    elif user_select == '2':
        add_contact()
    elif user_select == '3':
        search_contact()
    elif user_select == '4':
        delete_contact()
    else:
        print("Enter selection from menu")
def search_contact()->int|None:
    try:
        with open("contacts.json", 'r') as f:
            book = json.load(f)
            person_select = input("Please enter the name of the person: ")
            person_select = person_select.lower()
            for index, person in enumerate(book):
                name = next(iter(person))
                search_lower_name = name.lower()
                if search_lower_name == person_select:
                    pretty_print(person)
                    return index
            print("You have no contacts with that name.")
        return None
    except FileNotFoundError:
        print("You don't have any contacts yet. ")
        return None
def delete_contact()->None:
    person_to_delete = search_contact()
    with open("contacts.json", "r") as f:
        book = json.load(f)
        deleted_person = book.pop(person_to_delete)
    with open("contacts.json", "w") as f:
        json.dump(book, f, indent= 2)
        print(f"{deleted_person} was successfully deleted")