import socket
import pickle
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

HOST = 'localhost'  # Server IP address or hostname
PORT = 12345  # Port to connect to

# Function to send data to the server
def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(data.encode())

# Create a dictionary and send it to the server
def send_dictionary():
    dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    # Serialize the dictionary based on the pickling messageformat
    messageformat = input('Enter the pickling messageformat - (B)inary, (J)SON, or (X)ML:')
    if messageformat.upper == 'BINARY' or 'B':
        messageformat = 'BINARY'
        # we need to convert to string otherwise pickle has a wobbly when we decode
        serialized_dict = str(pickle.dumps(dictionary), 'Latin-1')
    elif messageformat.upper == 'JSON' or 'J':
        messageformat = 'JSON'
        serialized_dict = json.dumps(dictionary)
    elif messageformat.upper == 'XML' or 'X':
        messageformat = 'XML'
        serialized_dict = serialize_xml(dictionary)
    else:
        print('Unknown pickling messageformat')
        return

    # Send the serialized dictionary to the server
    data = 'DICT:{}:{}'.format(messageformat, serialized_dict)
    send_data(data)

# Function to serialize dictionary as XML
def serialize_xml(dictionary):
    root = ET.Element('dictionary')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    return ET.tostring(root).decode()

# Create a text file and send it to the server
def send_text_file():
    file_content = input('Enter the content of the text file: ')

    # Check if encryption is required
    encrypt = input('Encrypt the file content? (yes/no): ')
    if encrypt.lower() == 'yes':
        f = Fernet(b'hP9XQjOgbXJSOri9nSpeJ5oAXCRicT-e0hYd3tE7_ks=')
        encrypted_content = f.encrypt(file_content.encode())
        data = 'FILE:ENCRYPTED{}'.format(encrypted_content.decode())
    else:
        data = 'FILE:{}'.format(file_content)

    # Send the file content to the server
    send_data(data)

# Main program
while True:
    option = input('Enter 1 to send a dictionary or 2 to send a text file (0 to exit): ')
    if option == '0':
        break
    elif option == '1':
        send_dictionary()
    elif option == '2':
        send_text_file()
    else:
        print('Invalid option. Please try again.')
