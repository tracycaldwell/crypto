from helpers import alphabet_position, rotate_character   

def encrypt(text, rot):
    #receives string (text) and integer (rot)
    # return the result of rotating each letter in text by rot places to the right
    encrypted_list = []
    for i in text:
        encrypted_list.append(rotate_character(i, rot))
    return "".join(encrypted_list)

def main():
    # your main code (input and print statements)
    # text= input("Type a message:")
    # rot= input("Rotate by:")
    print(encrypt(text = input("Type a message:"), rot = input("Rotate by:")))


if __name__ == "__main__":
    main()
