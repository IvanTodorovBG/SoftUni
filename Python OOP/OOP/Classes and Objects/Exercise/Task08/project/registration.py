from project.user import User
from project.library import Library


class Registration:
    def __init__(self):
        pass

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for current_user in library.user_records:
            if current_user.user_id == user_id and current_user.username != new_username:
                # change username in rented books
                if current_user.username in library.rented_books:
                    library.rented_books[new_username] = library.rented_books[current_user.username]
                    del library.rented_books[current_user.username]
                # change username to new username
                current_user.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            elif current_user.user_id == user_id and current_user.username == new_username:
                return "Please check again the provided username - it " \
                       "should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"
