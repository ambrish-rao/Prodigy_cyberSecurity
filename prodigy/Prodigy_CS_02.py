#Encrypt or Decrypt the Image file Using Python Code

# To Create GUI we import tkinter
from tkinter import *
from tkinter import filedialog # filedialog is help to open the file box

root = Tk()
root.geometry("200x160")

def encrypt_image():
    file = filedialog.askopenfile(mode = 'r',filetypes = [('JPEG File','*.jpeg')]) # r is for extract the data and file type is for jpg or png file.
    if file is not None: # Our file variable is empty or not
        #print(file)# to print the file name 
        file_name = file.name
        #print(file_name) #exact path of the file
        key = entry1.get(1.0, END)
        print(file_name, key) # we exact file name and key.
        fil_open = open(file_name,"rb") #open image using 'rb'
        image = fil_open.read() # read and store in image variable
        fil_open.close()
        image = bytearray(image)#convert image into bytearray
        for index, values in enumerate(image): # enumerate to define the key for each values of this image variable.
            image[index] = values ^ int(key) #xor method '^'
        fil_open1 = open(file_name, "wb")
        fil_open1.write(image)
        fil_open1.close()


b1 = Button(root, text = "encrypt", command = encrypt_image) #for Buttom
b1.place(x = 70, y = 10) #buttom will present in x axis 70 and y axis 10

entry1 = Text(root, height = 1, width = 10) # root is for GUI and height and width is 1, 10 respectively..
entry1.place(x = 50, y = 50) # for center position.

root.mainloop()