import socket
import pickle
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

HOST = 'localhost'  # Server IP address or hostname
PORT = 12345  # Port to connect to

def send_data(data):
    """
    Send the provided data to the server using a TCP socket.

    Args:
        data (str): The data to be sent.

    Returns:
        None
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(data.encode())

def send_dictionary():
    """
    Create a dictionary, serialize it based on the chosen message format, and send it to the server.

    Returns:
        None
    """
    dictionary = {'Developer': 'Dillon', 'Tester': 'Lester', 'ProjectManager': 'Yasmin'}

    messageformat = input('Enter the pickling messageformat - (B)inary, (J)SON, or (X)ML:')
    if messageformat.upper() == 'B':
        messageformat = 'BINARY'
        serialized_dict = str(pickle.dumps(dictionary), 'Latin-1')
    elif messageformat.upper() == 'J':
        messageformat = 'JSON'
        serialized_dict = json.dumps(dictionary)
    elif messageformat.upper() == 'X':
        messageformat = 'XML'
        serialized_dict = serialize_xml(dictionary)
    else:
        print('Unknown pickling messageformat')
        return

    data = 'DICT:{}:{}'.format(messageformat, serialized_dict)
    send_data(data)

def serialize_xml(dictionary):
    """
    Serialize a dictionary as XML.

    Args:
        dictionary (dict): The dictionary to be serialized.

    Returns:
        str: The serialized XML data.
    """
    root = ET.Element('dictionary')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    return ET.tostring(root).decode()

def send_exit():
    """
    Send an exit message to the server.

    Returns:
        None
    """
    send_data('EXIT')

def send_text_file():
    """
    Create a text file, optionally encrypt it, and send its content to the server.

    Returns:
        None
    """
    file_content = input('Enter the content of the text file: ')

    encrypt = input('Encrypt the file content? (Y) or (N): ')
    if encrypt.upper() == 'Y':
        f = Fernet(b'hP9XQjOgbXJSOri9nSpeJ5oAXCRicT-e0hYd3tE7_ks=')
        encrypted_content = f.encrypt(file_content.encode())
        data = 'FILE:ENCRYPTED{}'.format(encrypted_content.decode())
    else:
        data = 'FILE:{}'.format(file_content)

    send_data(data)

if __name__ == '__main__':
    #Main program
    while True:
        option = input('Enter 1 to send a dictionary or 2 to send a text file (0 to exit):')
        if option == '0':
            send_exit()
            exit()
        elif option == '1':
            send_dictionary()
        elif option == '2':
            send_text_file()
        else:
            print('Invalid option. Please try again.')
