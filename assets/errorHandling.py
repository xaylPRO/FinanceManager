class UsernameExistsError(RuntimeError):
    def __init__(self):
        self.error = "Username alredy exists."

class PasswordDontMatch(RuntimeError):
    def __init__(self):
        self.error = "Previous password's doesn't match. Try again..."

class UserDontExist(RuntimeError):
    def __init__(self):
        self.error = "Requested users doesn't exist."
