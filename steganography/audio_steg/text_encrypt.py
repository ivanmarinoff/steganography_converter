# def text_encrypt(plaintext, hiddentext):
#     encrypted_text = ""
#     encrypted_text = plaintext + encrypted_text
#     for i in hiddentext:
#         whitespacecount = ord(i) - 31  # to save space
#         whitespacelist = [" "]*whitespacecount
#         encrypted_text = encrypted_text + ''.join(whitespacelist) + '\t'
#     return encrypted_text
#
# def text_decrypt(encrypted_text):
#     decrypted_text = ""
#     whitespacecount = 0
#     cipher_text = encrypted_text[0:len(encrypted_text)]  # remove end character
#     for i in encrypted_text:
#         if i == '\t':
#             decrypted_text = decrypted_text + chr(whitespacecount + 31)
#             whitespacecount = 0
#         elif i.isspace():
#             whitespacecount = whitespacecount + 1
#         elif i.isalpha():
#             whitespacecount = 0
#             continue
#     return decrypted_text
#
from steganography.audio_steg.models import *


def text_encrypt(plaintext, hiddentext):
    hiddentext = hiddentext.replace(" ", "")
    encrypted_text = plaintext + '\t'  # Add delimiter at the end
    for i in hiddentext:
        whitespacecount = ord(i) - 31  # to save space
        whitespacelist = [" "] * whitespacecount
        encrypted_text += ''.join(whitespacelist) + '\t'
    return encrypted_text


def text_decrypt(encrypted_text):
    decrypted_text = ""
    whitespacecount = 0
    for i in encrypted_text:
        if i == '\t':
            decrypted_text += chr(whitespacecount + 31)
            whitespacecount = 0
        elif i.isspace():
            whitespacecount += 1
        elif i.isalpha():
            decrypted_text += i
            whitespacecount = 0
    return decrypted_text


# def encode_text(input_text, secret_message, output_file):
#     binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
#     binary_message += '1111111111111110'  # Add a delimiter to mark the end of the message
#
#     with open(input_text, 'r') as file:
#         original_text = file.read()
#
#     encoded_text = list(original_text)
#     data_index = 0
#
#     for i in range(len(encoded_text)):
#         if data_index < len(binary_message):
#             encoded_text[i] = chr((ord(encoded_text[i]) & ~1) | int(binary_message[data_index]))
#             data_index += 1
#
#     with open(output_file, 'w') as file:
#         file.write(''.join(encoded_text))
#
#
# def decode_text(encoded_text):
#     with open(encoded_text, 'r') as file:
#         text_with_hidden_message = file.read()
#
#     binary_message = ''
#     for char in text_with_hidden_message:
#         binary_message += str(ord(char) & 1)
#
#     # Extract the message by finding the delimiter
#     message = ''.join(chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8))
#     end_index = message.find('\x00')  # Find the position of the delimiter
#     decoded_message = message[:end_index]
#
#     return decoded_message
#
#
# # Example usage:
# input_text = '../../steganography/steg_image/input/input.txt'
# secret_message = 'Hello, this is a secret message!'
# output_file = '../../steganography/steg_image/output/output.txt'
#
# # Encode the message
# encode_text(input_text, secret_message, output_file)
#
# # Decode the message
# decoded_message = decode_text(output_file)
# print("Decoded Message:", decoded_message)
