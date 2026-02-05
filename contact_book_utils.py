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