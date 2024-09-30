import socket
import pickle
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

HOST = 'localhost'  # Server IP address or hostname
PORT = 12345  # Port to listen on

def handle_data(data, action: str = 'PRINT', filename: str = ''):
    """
    Deserialize the received data and handle it based on its type.

    Args:
        data (str): The data received in the format "TYPE:CONTENT".

    Returns:
        None
    """
    data_type, content = data.split(':', 1)
    if data_type == 'DICT':
        handle_dictionary(content, action, filename)
    elif data_type == 'FILE':
        handle_file(content, action, filename)

def handle_dictionary(content, action, filename):
    """
    Deserialize the received dictionary based on the pickling message format and handle it.

    Args:
        content (str): The serialized dictionary in the format "FORMAT:SERIALIZED_DATA".
        action (str, optional): The action to perform with the dictionary. Options: 'print', 'save'. Defaults to 'print'.
        filename (str, optional): The name of the file to save the dictionary (if action is 'save'). Defaults to None.

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

    if action == 'PRINT':
        print(f'Received a dictionary in {messageformat}:')
        print(dictionary)
    elif action == 'SAVE' and filename:
        with open(filename, 'w') as file:
            file.write(str(dictionary))
            print(f'Dictionary saved to {filename}')

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

def handle_file(content, action, filename):
    """
    Handle the received file content, optionally decrypting it if encrypted.

    Args:
        content (str): The content of the file, with an optional "ENCRYPTED" prefix.
        action (str, optional): The action to perform with the file content. Options: 'print', 'save'. Defaults to 'print'.
        filename (str, optional): The name of the file to save the content (if action is 'save'). Defaults to None.

    Returns:
        None
    """
    if content.startswith('ENCRYPTED'):
        f = Fernet(b'hP9XQjOgbXJSOri9nSpeJ5oAXCRicT-e0hYd3tE7_ks=')
        content = f.decrypt(content[9:]).decode()

    if action == 'print':
        print('Received file content:')
        print(content)
    elif action == 'save' and filename:
        with open(filename, 'w') as file:
            file.write(content)
            print(f'File content saved to {filename}')

if __name__ == '__main__':
    #Main program
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
                    data = conn.recv(2048).decode()
                    if not data:
                        break

                    # Check for the escape command
                    if data.strip() == ESCAPE_COMMAND:
                        print("Escape command received. Closing the connection.")
                        exit()
                    
                    # Ask user whether to print or save the data
                    action = input("(P)rint or (S)ave the data?")
                    if action.upper()[0] == 'P':
                        handle_data(data)
                    # Cannot use an elif here because the filename does not get asked for?
                    elif action.upper()[0] == 'S':
                        filename = input("Enter the filename to save the data: ")
                        handle_data(data, action='SAVE', filename=filename)
                    else:
                        print("Invalid action. Please try again.")

            print('Waiting for new connection...')
