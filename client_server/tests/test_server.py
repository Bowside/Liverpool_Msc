import unittest
from unittest.mock import patch
import sys
import os
import socket
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import server app
import server as app

# Import test cases
from test_cases import(test_dict, test_file, result_binary, result_json, result_dict_xml)

class TestServerApp(unittest.TestCase):
    """
    Test cases for the server application.

    This class contains test cases to validate the functionality of the server application.
    It covers different scenarios for handling dictionaries and files, including printing and saving.

    Attributes:
    test_socket_client (socket.socket): A test socket client (mock) for testing the server's behavior.
    """

    def setUp(self):
        """
        Set up each test by creating a test socket client (mock).
        """
        
        print('Setting up test...')
        self.test_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def tearDown(self):
        """
        Tear down each test by closing the test socket client (mock).
        """
        
        print('Tearing down test...')
        self.test_socket_client.close()

    def test_handle_dictionary_print(self):
        """
        Test the handle_dictionary function with action=PRINT.

        This test verifies that the handle_dictionary function correctly prints the dictionary data.

        Raises:
        AssertionError: If the printed output does not match the expected dictionary.
        """

        print('Testing handle_dictionary_print function...')
        with patch('builtins.print') as mock_print:
            app.handle_dictionary(result_json, action='PRINT', filename=None)
            mock_print.assert_called_with(test_dict)

    def test_handle_dictionary_save(self):
        """
        Test the handle_dictionary function with action=SAVE.

        This test verifies that the handle_dictionary function correctly saves the dictionary data to a file.

        Raises:
        AssertionError: If the saved content does not match the expected dictionary.
        """

        print('Testing handle_dictionary_save function...')
        filename = f'{SCRIPT_DIR}\\test_dictionary.txt'
        with patch('builtins.print') as mock_print:
            app.handle_dictionary(result_json, action='SAVE', filename=filename)
            mock_print.assert_called_once_with(f'Dictionary saved to {filename}')

        # Check if the file was saved correctly
        with open(filename, 'r') as file:
            saved_content = file.read()
            self.assertEqual(str(test_dict), saved_content)

    def test_parse_xml(self):
        """
        Test the parse_xml function.

        This test verifies that the parse_xml function correctly converts XML data to a dictionary.

        Raises:
        AssertionError: If the parsed dictionary does not match the expected dictionary.
        """

        print('Testing parse_xml function...')
        self.assertEqual(app.parse_xml(result_dict_xml), test_dict)

    def test_handle_file_print(self):
        """
        Test the handle_file function with action=print.

        This test verifies that the handle_file function correctly prints the file content.

        Raises:
        AssertionError: If the printed output does not match the expected file content.
        """

        print('Testing handle_file_print function...')
        with patch('builtins.print') as mock_print:
            app.handle_file(test_file, action='print', filename=None)
            mock_print.assert_called_with(test_file)

    def test_handle_file_save(self):
        """
        Test the handle_file function with action=SAVE.

        This test verifies that the handle_file function correctly saves the file content to a file.

        Raises:
        AssertionError: If the saved content does not match the expected file content.
        """

        print('Testing handle_file_save function...')
        filename = f'{SCRIPT_DIR}\\test_file.txt'
        with patch('builtins.print') as mock_print:
            app.handle_file(test_file, action='save', filename=filename)
            mock_print.assert_called_once_with(f'File content saved to {filename}')

        # Check if the file was saved correctly
        with open(filename, 'r') as file:
            saved_content = file.read()
            self.assertEqual(saved_content, test_file)

if __name__ == '__main__':
    unittest.main()
