import os


def clear():
    os.system('clear')


title = """
___  ___                      _____           _        _____                           _            
|  \/  |                     /  __ \         | |      /  __ \                         | |           
| .  . | ___  _ __ ___  ___  | /  \/ ___   __| | ___  | /  \/ ___  _ ____   _____ _ __| |_ ___ _ __ 
| |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \ / _` |/ _ \ | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |  | | (_) | |  \__ \  __/ | \__/\ (_) | (_| |  __/ | \__/\ (_) | | | \ V /  __/ |  | ||  __/ |   
\_|  |_/\___/|_|  |___/\___|  \____/\___/ \__,_|\___|  \____/\___/|_| |_|\_/ \___|_|   \__\___|_|   


"""

morse_code = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
              "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
              "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--..",
              }


continue_converting = True

while continue_converting:

    print(title)
    text_to_convert = input("Type the text you want to convert into morse code: ").upper()

    converted_text = []
    for letter in text_to_convert:
        converted_text.append(morse_code[letter])

    morse_code_text = " ".join(converted_text)

    print(f"Your text input was: {text_to_convert}, your morse code output is: {morse_code_text}")

    quit_converter = input("Do you want to quit the converter? If so, type 'Y', otherwise type 'N': ").upper()

    if quit_converter == "Y":
        continue_converting = False

    clear()
