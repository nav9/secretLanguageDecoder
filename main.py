from loguru import logger as log

def encode_decode_text(text, string1, string2):
    result = ""
    for char in text:
        index = string2.find(char)
        if index != -1:
            result += string1[index]
        else:
            result += char
    return result

def read_cipher_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            string1 = lines[0].strip()
            string2 = lines[1].strip()
            return string1, string2
    except FileNotFoundError:
        log.error("Cipher file not found. Please make sure 'cipher.txt' exists.")
        return None, None

def main():
    filename = "text.txt" 
    cipher_filename = "cipher.txt"
    example_string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    example_string2 = "ZYXWVUTSRQPONMLKJIHGFEDCBA0987654321"    
    log.info(f"Welcome to Secret Language Encoder Decoder. The text to encode or decode should be in a "\
              f"file named {filename} and the cipher strings should be in a file named {cipher_filename}."\
              f"\nAn example of cipher strings are {example_string1} and {example_string2}. They should be "\
              f"placed in separate lines in {cipher_filename} without quotes.\n\n")

    string1, string2 = read_cipher_file(cipher_filename)

    if string1 is None or string2 is None or len(string1) != len(string2):
        raise ValueError(f"You need to place cipher strings of equal length in {cipher_filename}. Strings loaded are `{string1}` and `{string2}`.")
    
    text = ""
    try:
        with open(filename, 'r') as file:
            text = file.read().strip()
    except FileNotFoundError:
        log.error("File not found. Please enter a valid filename.")
        return    
    
    text.upper()
    result = encode_decode_text(text, string1, string2)

    log.info(f"Result: \n{result}")

if __name__ == "__main__":
    main()

