def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using Caesar cipher algorithm.
    
    Parameters:
        text (str): The input text to process
        shift (int): The number of positions to shift each character
        mode (str): 'encrypt' or 'decrypt'
    
    Returns:
        str: The processed text
    """
    result = ""
    
    # If decrypting, reverse the shift direction
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isupper():
            # Shift uppercase characters
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Shift lowercase characters
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    print("----------------------")
    
    while True:
        # Get user input
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if mode not in ['e', 'd']:
            print("Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
            
        text = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if not 1 <= shift <= 25:
                print("Shift must be between 1 and 25")
                continue
        except ValueError:
            print("Please enter a valid number for the shift.")
            continue
            
        # Process the message
        if mode == 'e':
            processed_text = caesar_cipher(text, shift, 'encrypt')
            print(f"Encrypted message: {processed_text}")
        else:
            processed_text = caesar_cipher(text, shift, 'decrypt')
            print(f"Decrypted message: {processed_text}")
            
        # Ask if user wants to continue
        another = input("Process another message? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()