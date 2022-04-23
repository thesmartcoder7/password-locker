import random
import pyperclip

characters = [
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']


def generate_password():
    r_letters = [random.choice(characters) for _ in range(7)]
    r_numbers = [random.choice(numbers) for _ in range(7)]
    r_symbols = [random.choice(symbols) for _ in range(7)]
    gen_password = r_letters + r_numbers + r_symbols
    random.shuffle(gen_password)
    generated_password = "".join(gen_password)
    return generated_password
