# password Complexity Checker
# 8 charecter in length minimum which incliude
# 1 Uppercase
# 1 lowercase
# 1 digit
# 1 Symbol
import re # re module is used to which allow to search and match patterns in strings

while True:
 # It ensures that the programe will keep running until password is valid...
    password = input("Enter Your Password: ")

    # Password must be at least 8 characters long
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    
    # Password must contain at least one uppercase letter
    elif not re.search('[A-Z]', password):
        print("Password must contain at least one uppercase letter.")
    
    # Password must contain at least one lowercase letter
    elif not re.search('[a-z]', password):
        print("Password must contain at least one lowercase letter.")
    
    # Password must contain at least one number
    elif not re.search('[0-9]', password):
        print("Password must contain at least one number.")
    
    # Password must contain at least one symbol
    elif not re.search('[!@#$%^&*()_+}{|\":<>?~,.]', password):
        print("Password must contain at least one symbol.")
    
    # If all conditions are satisfied
    else:
        print("Password is strong!")
        break  # Exit the loop if the password is valid
