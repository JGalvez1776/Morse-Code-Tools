from utils import *

LETTER_TO_ROMAN = {
                'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                'E': '.' , 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
                'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
                'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
                '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
                ':': '---...',  ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
                '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.',
                ' ': '     '
            }

MORSE_TO_LETTER = {value: key for (key, value) in LETTER_TO_ROMAN.items()}

def convert_to_morse(data):
    # Maybe find a way to make translation be a list converted to a string?
    translation = ''
    for character in data.upper():
        translation += LETTER_TO_ROMAN[character] + ' '
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
    # Main is to be used in testing. Remove once the program is finished.
    phrase = 'SOS THIS MESSAGE HERE IS TO TEST THE AUDIO!'
    phrase2 = convert_to_morse(phrase)
    print('Originals:')
    print(phrase)
    print(phrase2)
    print('\nTranslations')
    output_morse(phrase2, 250)

if __name__ == '__main__':
    main()
