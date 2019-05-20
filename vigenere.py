from helpers import alphabet_position, rotate_character

def encrypt(text, key):
# take first letter of message if alpha
# rotate by index of first letter of key
# return new letter
    encrypted_list = []
    key_counter = 0
    for i in text:
        if i.isalpha() == True:
            rot = alphabet_position(key[key_counter])
            if key_counter < (len(key)-1):
                key_counter += 1
            else:
                key_counter = 0
        encrypted_list.append(rotate_character(i, rot))

    return "".join(encrypted_list)
def main():
    print(encrypt(text = input("Type a message:"), key = input("Encryption key:")))


if __name__ == "__main__":
    main()
