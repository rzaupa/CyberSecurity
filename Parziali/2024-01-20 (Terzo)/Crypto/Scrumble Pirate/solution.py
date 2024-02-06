def replace_chars(input_string, char_dict):
    result = ""
    for char in input_string:
        result += char_dict.get(char, char)
    return result

with open("challenge.txt", "r") as file:
    cipher = ''.join(file.readlines())
    
dictionary = {'D':'s','M':'p','P':'r','X':'i','S':'t','T':'z','H':'a','L':'e','A':'h','R':'u','E':'o','O':'n','Z':'c','V':'f','Y':'d','W':'g','Q':'k','U':'l'}
text = replace_chars(cipher, dictionary)
print(text)
