import os
import base64
import pyperclip

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('''
[1] Encode Message
[2] Decode Message
''')

def main():
    while True:
        clear()
        menu()
        choice = input('[>>>] ')
        if choice.lower() == 'encode message' or choice == '1':
            clear()
            print('Enter the message to encode:')
            message = input('[>>>] ')
            clear()
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print('Here is your encoded text:')
            print(base64_message)
            pyperclip.copy(base64_message)
            print('Copied to Clipboard')
            print('\nPress any key to return')
            input()
        elif choice.lower() == 'decode message' or choice == '2':
            clear()
            print('Enter the message to decode:')
            base64_message = input('[>>>] ')
            clear()
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            print('Here is your encoded text:')
            print(message)
            pyperclip.copy(message)
            print('Copied to Clipboard')
            print('\nPress any key to return')
            input()

main()
        
