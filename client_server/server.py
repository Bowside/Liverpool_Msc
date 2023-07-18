import socket
import pickle
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

HOST = 'localhost'  # Server IP address or hostname
PORT = 12345  # Port to listen on

# Function to handle received data
def handle_data(data):
    # Deserialize the data and handle based on its type
    data_type, content = data.split(':', 1)
    if data_type == 'DICT':
        handle_dictionary(content)
    elif data_type == 'FILE':
        handle_file(content.encode())

# Function to handle received dictionary
def handle_dictionary(content):
    # Deserialize the dictionary based on the pickling messageformat
    try:
        messageformat, serialized_dict = content.split(':', 1)
        if messageformat == 'BINARY':
            # we need to convert the string back to bytes otherwise pickle has a wobbly
            dictionary = pickle.loads(bytes(serialized_dict, 'latin-1'))
        elif messageformat == 'JSON':
            dictionary = json.loads(serialized_dict)
        elif messageformat == 'XML':
            dictionary = parse_xml(serialized_dict)
        else:
            print('Unknown pickling message format')
            return
    except Exception as e:
        print(e)
        return
    # Print or store the dictionary contents
    print('Received dictionary:')
    print(dictionary)

# Function to parse XML data
def parse_xml(xml_data):
    root = ET.fromstring(xml_data)
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary

# Function to handle received text file
def handle_file(content):
    # Check if the content is encrypted
    if content.startswith('ENCRYPTED'):
        # Decrypt the content
        f = Fernet(b'your-encryption-key')
        content = f.decrypt(content[9:]).decode()

    # Print or store the file contents
    print('Received file content:')
    print(content)

# Start the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print('Server listening on {}:{}'.format(HOST, PORT))

    conn, addr = server_socket.accept()
    print('Connected by', addr)

    with conn:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            handle_data(data)

        print('Connection closed.')
