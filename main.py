from utils import *

LETTER_TO_MORSE = {
                'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                'E': '.' , 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
                'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
                'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
                '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', 
                '(': '-.--.', ':': '---...',  ',': '--..--', '=': '-...-', 
                '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.', 
                '"': '.-..-.', '?': '..--..', '/': '-..-.', ' ': '     '
            }

MORSE_TO_LETTER = {value: key for (key, value) in LETTER_TO_MORSE.items()}

def convert_to_morse(data):
    # Maybe find a way to make translation be a list converted to a string?
    translation = ''
    for character in data.upper():
        if character not in LETTER_TO_MORSE:
            assert False, f'ERROR: "{character}" is not translateable into morse code.'
        translation += LETTER_TO_MORSE[character] + ' '
    return translation[:-1]

def convert_to_roman(data):
    counter = 0
    translation = ''
    for character in data.split(' '):
        if character == '':
            counter += 1
            if counter == 6:
                counter = 0
                translation += ' '
        else:
            translation += MORSE_TO_LETTER[character]
    return translation

def main():
    # NOTE: Implement spaces in the morse code translations
    phrase = input('Orignal input:\n')
    if phrase[0] in ['.', '-']:
        phrase2 = convert_to_roman(phrase)
        msg = 'Morse to Roman'
    elif phrase[0] in LETTER_TO_MORSE:
        # NOTE: Having a space then Morse code still ends up here!
        phrase2 = convert_to_morse(phrase)
        msg = 'Roman to Morse'
    else:
        assert False, 'Invalid Characters enterd'
    print(f'\nTranslation')
    print(phrase2)
    print(f'({msg})')


if __name__ == '__main__':
    main()
