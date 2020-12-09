'''
Project 2 - Secret Codes - Fall 2020
Author: <Nicholas Rooks 9063-32432>

<ceaser cypher program

I have neither given or received unauthorized assistance on this assignment.
Signed:  <Nicholas Rooks>  
'''
def encrypt(message, shift):
    result = ''

    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    print(result)
        
def decrypt(message, shift):
    result = ''

    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) - shift))
            
        else:
            result += chr((ord(char) - shift))
    print(result)
    
def get_shift_factor():
    shift = int(input('shift factor? '))
    while shift <= 0:
        print('ERROR - SHIFT FACTOR must be GREATER than ZERO')
        shift = int(input('Reenter shift factor '))
    return shift
            
    
    

def main():
    print("Welcome to Cryptic2020!")
    q = 0
    shift = 0
            
    while q is not 1:
        option = input("Encrypt (E), Decrypt (D), or Quit (Q)? ")
        if option == ('Q'):
            q = q + 1
            break
        
        
        elif option== ('E'):
            message = input('Original Message? ')
            shift = get_shift_factor()
            encrypt(message, shift)

        
        elif option==('D'):
            message = input('Encrypted Message? ')
            get_shift_factor()
            decrypt(message, shift)
            
            
    print('Thanks for using Cryptic2020!')

    
if __name__ == '__main__':
    main()