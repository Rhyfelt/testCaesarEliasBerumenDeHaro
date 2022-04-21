from sys import argv

def get_encripted_character(character, ascii_firstletter_code, k_positions):
    ascii_code = ord(character)
    encripted_character = ""
    code_rotated = k_positions+(ascii_code-ascii_firstletter_code)
    if code_rotated >= 26:
        residual = code_rotated % 26
        encripted_character_code = residual + ascii_firstletter_code
        encripted_character = chr(encripted_character_code)
    else:
        encripted_character = chr(ascii_code+k_positions)
    return encripted_character
           

def encoding(k_positions, plaintext):
    message_encoded_list = []
    for character in plaintext:
        if character.isalpha():
            if character.isupper():
                encripted_character = get_encripted_character(character,65,k_positions)
                message_encoded_list.append(encripted_character) 
            else:
                encripted_character = get_encripted_character(character,97,k_positions)
                message_encoded_list.append(encripted_character)
        else:
            message_encoded_list.append(character)
    message_encoded = ''.join([character for character in message_encoded_list])
    return message_encoded


def main():

    if len(argv) > 2 or len(argv) == 1:
        print("Error: you need to provide only one non-negative integer number")
        raise "status code 1"
    
    k_positions = argv[1]

    plaintext = input('plaintext: ')

    ciphertext = encoding(k_positions=int(k_positions), plaintext=plaintext)

    print('ciphertext: ', ciphertext)
    print('')



if __name__ == '__main__':
    main()