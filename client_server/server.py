import socket
import pickle
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

HOST = 'localhost'  # Server IP address or hostname
PORT = 12345  # Port to listen on

def handle_data(data):
    """
    Deserialize the received data and handle it based on its type.

    Args:
        data (str): The data received in the format "TYPE:CONTENT".

    Returns:
        None
    """
    data_type, content = data.split(':', 1)
    if data_type == 'DICT':
        handle_dictionary(content)
    elif data_type == 'FILE':
        handle_file(content)

def handle_dictionary(content):
    """
    Deserialize the received dictionary based on the pickling message format and handle it.

    Args:
        content (str): The serialized dictionary in the format "FORMAT:SERIALIZED_DATA".

    Returns:
        None
    """
    try:
        messageformat, serialized_dict = content.split(':', 1)
        if messageformat == 'BINARY':
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

    print(f'Received a dictionary in {messageformat}:')
    print(dictionary)

def parse_xml(xml_data):
    """
    Parse XML data and convert it to a dictionary.

    Args:
        xml_data (str): The XML data to be parsed.

    Returns:
        dict: The dictionary obtained from the parsed XML data.
    """
    root = ET.fromstring(xml_data)
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary

def handle_file(content):
    """
    Handle the received file content, optionally decrypting it if encrypted.

    Args:
        content (str): The content of the file, with an optional "ENCRYPTED" prefix.

    Returns:
        None
    """
    if content.startswith('ENCRYPTED'):
        f = Fernet(b'hP9XQjOgbXJSOri9nSpeJ5oAXCRicT-e0hYd3tE7_ks=')
        content = f.decrypt(content[9:]).decode()

    print('Received file content:')
    print(content)

# Define the escape command that will terminate the server
ESCAPE_COMMAND = "EXIT"

# Start the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print('Server listening on {}:{}'.format(HOST, PORT))

    while True:  # Keep the server running in an infinite loop
        conn, addr = server_socket.accept()
        print('Connected by', addr)
        print('Waiting for data...')

        with conn:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break

                # Check for the escape command
                if data.strip() == ESCAPE_COMMAND:
                    print("Escape command received. Closing the connection.")
                    break

                handle_data(data)

        print('Waiting for new connection...')
