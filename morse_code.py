
# Bai 5
# This quite a silly question since we have a code the only thing we must do is to encode it :D

if __name__ == "__main__":
    morse_code = ".- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ...."
    characters_encoding = morse_code.split(' ')
    morse_code_dict = { 'A':'.-', 'B':'-...',
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
    reverse_morse_code_dict = {}
    encoding_text = ""
    for key, value in morse_code_dict.items():
        reverse_morse_code_dict[value] = key
    for letter in characters_encoding:
        encoding_text += reverse_morse_code_dict[letter] + ' '
    print(encoding_text)  # A L L I W A N T T O S A Y I S D O T D O T S P A C E D O T D A S H D O T D O T S P A C E D A S H D A S H D A S H S P A C E D O T D O T D O T D A S H S P A C E D O T S P A C E D A S H D O T D A S H D A S H S P A C E D A S H D A S H D A S H S P A C E D O T D O T D A S H 

