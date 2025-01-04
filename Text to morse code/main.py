MORSE_CODE_DICTIONARY = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def text_to_morse_code(string):
    message = ''
    if string == '':
        return 'Invalid choice'
    for character in string:
        current_char = character
        if character == ' ':
            message += '  '
        elif current_char in MORSE_CODE_DICTIONARY:
            message += MORSE_CODE_DICTIONARY[current_char]
            message+=' '


    return message.strip()


text_to_encrypt = input('Enter a text to translate to morse code: \n').upper()
result = text_to_morse_code(text_to_encrypt)
print(f'Here is the result: {result}')