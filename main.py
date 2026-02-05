from contact_book_utils import *
if __name__ == "__main__":
    while True:
        show_menu()
        user_selection = input("Please enter your choice: ")
        if user_selection == 'quit':
            break
        menu_selection(user_selection)