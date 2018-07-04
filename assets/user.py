import os
from .errorHandling import UsernameExistsError  # This module includes custom error handling
from .encryption import encrypt, decrypt


def checkFile():  # Function is goingto check if needed directory accounts and needed user_accounts.txt file is alredy created
    if(os.path.isdir("accounts")):  # If account is created:
        if(os.path.isfile("accounts/user_accounts.txt")):  # Check the existence of the file
            return True  # Return true, both file and directory are created
        else:  # If directory exists but file isn't crated:
            file = open("accounts/user_accounts.txt", 'w')  # Crate a new file named user_accounts.txt
            file.close()  # Close the file to avoid any complications
            return True  # File and directory are created, return bool value True

    else:  # Else id directory doesn't exists:
        os.mkdir("accounts")  # Create the directory
        file = open("accounts/user_accounts.txt")  # Crate needed text files
        file.close()  # Colose file to avoid any complications later
        return True  # Both file and directory are created, return bool value False

class Login:
    __username = None
    __password = None
    __d = {}
    def __init__(self, username, password):
        # Class Login on initialization needs two parameters, username and password
        self.__username = username
        self.__password = password
        if(checkFile()):  # On initilization we're going to check if there is crated our directory and the needed txt file with our previus declared function "checkFile()"
            current_file = open("accounts/user_accounts.txt", 'r')  # If file and directory exist, open txt file
            user_accounts = current_file.read();  # Read all usernames and password from the file
            current_file.close()
            word = ""
            position = 1
            index = ""
            for i in user_accounts:  # Now we're going to extract usernames and passwords from string user_accounts
                if (i != ":"):
                    word += i
                elif (position == 1):
                    self.__d[word] = 0
                    index = word
                    word = ""
                    position += 1
                elif (position == 2):
                    self.__d[index] = word
                    position = 1
                    index = ""
                    word = ""


    def verify(self):  # We got all existing usernames and password, now we're going to match if there is any that eqials to provides username and password
        for username in self.__d:  # Frpm our dict we will get our username witha for loop
            password = self.__d[username]  # Getting the peassword related to our username
            if (decrypt(username) == self.__username and decrypt(password) == self.__password):  # Checking if any of the username-password pair equals to the provided pair
                return True  # If there is any pair return bool value True
        return False  # If there isn't any match return False

class User:
    __d = {}  # All username-password pairs will be stored here
    def __init__(self):  # On initialization username-password pairs are going to be extracted
        if(checkFile()):
            current_file = open("accounts/user_accounts.txt", 'r')
            user_accounts = current_file.read();
            current_file.close()
            word = ""
            position = 1
            index = ""
            for i in user_accounts:
                if (i != ":"):
                    word += i
                elif (position == 1):
                    self.__d[word] = 0
                    index = word
                    word = ""
                    position += 1
                elif (position == 2):
                    self.__d[index] = word
                    position = 1
                    index = ""
                    word = ""

    def UsernameExists(self, new_username):  # Function is going to check if wanted username alredy exists
        for username in self.__d:  # Checking the dict with previous provided usernames for any matches
            if(username == encrypt(new_username)):  # If there is a match return bool value True
                return True
        return False  # If tehere isn't any match return bool value False

    def CreateNew(self, username, password):  # Function will write our new user's password and username to our user_accounts txt file
        if(self.UsernameExists(username)):  # Checking for similiar usernames
            raise UsernameExistsError  # If tehere are similiar usernames rais error
        else:  # If it's a unique username:
            current_file = open("accounts/user_accounts.txt", 'a') # Open file user_accounts.txt
            to_write = encrypt(username) + ":" + encrypt(password) + ":"  # merge username and password in one string so that there are divided by ":"
            current_file.write(to_write)  # Write the string to our file
            current_file.close()  # Close file
            return True  # Return bool value True

    def allUsers(self):  # All existing users are going to be stored in one list:
        users = []
        for user in self.__d:
            users.append(user)  # Storing all users to the list

        return users  # Returning created list

    def removeUser(self, target_username):
        target_username = encrypt(target_username)
        to_remove = None
        for username in self.__d:
            if(username == target_username):
                to_remove = username
                print(to_remove)
                del self.__d[to_remove]
                break


        print(self.__d)

        current_documnet = open("accounts/user_accounts.txt", 'w')
        to_write = ""
        for j in self.__d:
            to_write += j + ":"
        to_write = to_write[0:len(to_write)-1]

        current_documnet.write(to_write)

        return True

    def ChangeUsername(self, current_username, new_username):
        for i in self.__d:
            if decrypt(i) == current_username:
                password = self.__d[i]
                self.removeUser(decrypt(i))
                break
        self.CreateNew(new_username, password)

    def ChangePassword(self, target_username, current_password, new_password):

        for username in self.__d:
            if(username == encrypt(target_username)):
                if(encrypt(current_password) == self.__d[username]):
                    del self.__d[username]
                    self.__d[username] = encrypt(new_password)

                    current_file = open("accounts/user_accounts.txt", 'w')
                    to_write = ""
                    for i in self.__d:
                        to_write += i + ":" + self.__d[i] + ":"
                    current_file.write(to_write)
                    current_file.close()
                    return True
                else:
                    raise PasswordDontMatch
            else:
                raise UserDontExist
            return False

#login_user = Login("jasmin", "1234")
#print(login_user.verify())
#new_user = User()
#new_user.CreateNew("Stan Markale", "3009")













