# from steganography.audio_steg.text_encrypt import encode_text
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
# input_text = '../../steganography/steg_image/output/output.txt'
# secret_message = 'Hello, this is a secret message!'
# output_file = '../../steganography/steg_image/output/decode.txt'
#
# encode_text(input_text, secret_message, output_file)
#
# decoded_message = decode_text(output_file)
# print("Decoded Message:", decoded_message)

