alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def alphabet_position(letter):
    # receives letter & returns index position (case insensitive)
    return alphabet.index(letter.upper())

def rotate_character(char, rot):
    #recives character (char) and an integer (rot)
    #rotate char by rot places to the right
    if char.isalpha() == False:
        return char

    current_index = int(alphabet_position(char))
    new_index = (current_index + int(rot)) % 26
    #return new string of length 1
    # return alphabet[new_index]
    if char.isupper() == True:
        return alphabet[new_index]
    
    return alphabet_lower[new_index]
