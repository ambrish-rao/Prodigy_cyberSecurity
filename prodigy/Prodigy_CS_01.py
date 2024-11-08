'''Create a Python program that can encript and decrypt text using the Caesar Cipher Algorithm.
Allow User to input a message and a shift value to perform encryption and decryption.'''

'''for Encription formulla is :
E(x) = (X + n)mod 26
Where,
X = Alphabet(A-Z) position (index)
n = shift key'''

'''for Decription formulla is :
D(x) = (X - n)mod 26
Where,
X =  position of that letter which we encripted (index)
n = shift key'''

# when the value is -ve then we add 26 to make it positive

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # It is based on index
def encryption(plane_text, shift_key): # This function will encript the code.
    cipher_text = ""

    for char in plane_text: # Tis loop is find the alphabet and change a/c to the shift key
        if char in alpha: # if we enter numeric value, Special Symbole,Spaces then it will print as same as given.
            position = alpha.index(char) 
            new_position = (position + shift_key) % 26
            cipher_text += alpha[new_position]
        else:
            cipher_text += char

    print(f"Here's is the text after Encriptions : {cipher_text}")

def decryption(cipher_text, shift_key): # hello h= 7 index
    plane_text = ""

    for char in cipher_text: # Tis loop is find the alphabet and chacge a/c to the shift key.
        if char in alpha: # if we enter numeric value, Special Symbole,Spaces then it will print as same as given.
            position = alpha.index(char) 
            new_position = (position - shift_key) % 26
            plane_text += alpha[new_position]
        else:
            plane_text += char

    print(f"Here's is the text after Decriptions : {plane_text}")

end = False
while not end:
    type = input("Type 'encrypt' for encryption, Type'decrypt' for decryption : ")
    text = input("Type your Message : ").lower() # if we enter capital letter then it will convert lower letter.
    shift = int(input("Enter Shift Key : "))
    if type == "encrypt":
        encryption(plane_text = text, shift_key = shift)
    elif type == "decrypt":
        decryption(cipher_text = text,shift_key = shift)
    else:
        print("Invalid ! Please enter 'encrypt' or 'decrypt' ")
    again = input("Type 'yes' to continue, and 'no' for exit : ")
    if again == 'no':
        end = True
        print("Thank U. Have a Nice Day!, Bye....")
