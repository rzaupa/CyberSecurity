import base64


morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
    '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',
    '/': ' ', '': ' ',
    '.-.-.-': '.', '--..--': ',', '..--..': '?',
    '.----.': "'", '-.-.--': '!', '-..-.': '/',
    '-.--.': '(', '-.--.-': ')', '.-...': '&',
    '---...': ':', '-.-.-.': ';', '-...-': '=',
    '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@'
}

def morse_to_text(morse_code):
    words = morse_code.split('   ')  # Words are separated by three spaces
    decoded_text = ''
    
    for word in words:
        letters = word.split(' ')  # Letters are separated by one space
        for letter in letters:
            decoded_text += morse_code_dict.get(letter, '?')
        decoded_text += ' '
    
    return decoded_text.strip()

# Example usage:
with open('cyphertext.txt', 'r') as file:
    text = file.read().strip()
    
def decode_base64(text):
    return base64.b64decode(text).decode('utf-8')

morse_code = text.split('\n')[0]
second_part= text.split('\n')[1]
decoded_morse_text = morse_to_text(morse_code)
#print(decoded_morse_text)
decoded_base64_text = decode_base64(second_part)
#print(decoded_base64_text)
# print(second_part)

brute_force_part=decoded_base64_text.split('\n')[0]
brute_force_part=brute_force_part.replace('V', 'I').replace('g','t').replace('u','h').replace('r','e').replace('z','m').replace('n','a').replace('q','d').replace('b','o').replace('p','c').replace('s','f').replace('a','n').replace('h','u')
print(brute_force_part)