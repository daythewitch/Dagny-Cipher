import random

# Define letter categories
dit_letters = "aweiruoszxcvnm"
dah_letters = "qtypdfghjklb"

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.", 'H': "....", 'I': "..",
    'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...",
    'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--.."
}

# Reverse Morse code dictionary
REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def random_letter(morse_symbol):
    """Returns a random letter from the appropriate category based on Morse symbol."""
    if morse_symbol == '.':
        return random.choice(dit_letters)
    elif morse_symbol == '-':
        return random.choice(dah_letters)
    return ''

def text_to_gibberish(text):
    """Converts input text into a gibberish cipher based on the Morse code representation."""
    text = text.lower().rstrip('.')
    words = text.split()
    gibberish_words = []

    for word in words:
        gibberish_word = ' '.join(
            ''.join(random_letter(symbol) for symbol in MORSE_CODE_DICT.get(letter.upper(), ''))
            for letter in word
        )
        gibberish_words.append(gibberish_word)

    return ', '.join(gibberish_words)

def gibberish_to_text(gibberish):
    """Decodes gibberish back into text based on Morse code mappings."""
    word_groups = gibberish.split(', ')
    decoded_words = []
    
    for group in word_groups:
        words = group.split()
        decoded_word = ''.join(
            REVERSE_MORSE_DICT.get(
                ''.join('-' if letter in dah_letters else '.' if letter in dit_letters else '' for letter in word),
                '?'  # Default if not found
            ) for word in words
        )
        decoded_words.append(decoded_word)
    
    sentence = ' '.join(decoded_words).capitalize() + '.'
    return sentence

def display_morse_code():
    """Displays the Morse code dictionary."""
    for letter, code in MORSE_CODE_DICT.items():
        print(f"{letter}: {code}")

if __name__ == "__main__":
    print("\n·▄▄▄▄   ▄▄▄·  ▄▄ •  ▐ ▄  ▄· ▄▌█  .▄▄ ·    ▄▄· ▪   ▄▄▄· ▄ .▄▄▄▄ .▄▄▄  ")
    print("██· ██ ▐█ ▀█ ▐█ ▀ ▪•█▌▐█▐█▪██▌   ▐█ ▀.   ▐█ ▌▪██ ▐█ ▄███▪▐█▀▄.▀·▀▄ █·")
    print("▐█▪ ▐█▌▄█▀▀█ ▄█ ▀█▄▐█▐▐▌▐█▌▐█▪   ▄▀▀▀█▄  ██ ▄▄▐█· ██▀·██▀▀█▐▀▀▪▄▐▀▀▄ ")
    print("██. ██ ▐█▪ ▐▌▐█▄▪▐███▐█▌ ▐█▀·.   ▐█▄▪▐█  ▐███▌▐█▌▐█▪·•██▌▐▀▐█▄▄▌▐█•█▌")
    print("▀▀▀▀▀•  ▀  ▀ ·▀▀▀▀ ▀▀ █▪  ▀ •     ▀▀▀▀   ·▀▀▀ ▀▀▀.▀   ▀▀▀ · ▀▀▀ .▀  ▀")
    print("\n")
    
    while True:
        choice = input("Enter 'e' to encode, 'd' to decode, 'm' to display Morse code, or 'q' to quit: ").strip().lower()
        if choice == 'q':
            break
        elif choice == 'e':
            user_input = input("Enter a letter or word to encode: ")
            result = text_to_gibberish(user_input)
            print(f"Gibberish output: {result}")
        elif choice == 'd':
            user_input = input("Enter gibberish to decode: ")
            result = gibberish_to_text(user_input)
            print(f"Decoded text: {result}")
        elif choice == 'm':
            display_morse_code()
        print("----------------------------")
