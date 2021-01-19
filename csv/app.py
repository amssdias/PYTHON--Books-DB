from utils import database

USER_cHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""


def menu():
    database.create_book_table()
    menu = {
        'a': prompt_add_book,
        'l': list_books,
        'r': prompt_read_book,
        'd': prompt_delete_book
    }

    user_input = input(USER_cHOICE)

    while user_input != 'q':
        try:
            user_option = menu[user_input]
            user_option()
        except KeyError:
            print('Unknown command. Please try again.')

        user_input = input(USER_cHOICE)


# ask for book name and author
def prompt_add_book():
    name = input('Book name: ')
    author = input('Book author: ')
    database.add_book(name, author)


# show all the books in our list
def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}.")


# ask for book name and change it to "read" in our list
def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')
    database.mark_book_as_read(name)


# ask for book name and remove book from list
def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')
    database.delete_book(name)

menu()