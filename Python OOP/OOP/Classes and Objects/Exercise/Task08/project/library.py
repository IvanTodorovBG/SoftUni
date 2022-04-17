from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available:
            # available
            if book_name in self.books_available[author]:
                # remove book from books_available
                self.books_available[author].remove(book_name)
                # add book to user books list
                user.books.append(book_name)
                # add book to rented_books
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                if book_name not in self.rented_books[user.username]:
                    self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"
            else:
                return f'The book "{book_name}" is already rented and will be available in ' \
                       f'{self.rented_books[user.username][book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            # add book to books_available
            self.books_available[author].append(book_name)
            # remove book from rented_books
            del self.rented_books[user.username][book_name]
            # remove the user from user`s book list
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"