from cryptography.fernet import Fernet
import unittest
from unittest.mock import patch
import sys
import os
import socket

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import the client application
import client as app

# Import the tests cases
from test_cases import(test_dict, test_file, result_dict_binary, result_dict_json, result_dict_xml, result_file1, result_file2)

class TestApp(unittest.TestCase):

    def setUp(self):
        print('Setting up test...')
        # Create a test socket server (mock) for testing send_data function
        self.test_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.test_socket_server.bind((app.HOST, app.PORT))
        self.test_socket_server.listen(1)

    def tearDown(self):
        print('Tearing down test...')
        # Close the test socket server (mock) after each test
        self.test_socket_server.close()

    def test_send_dictionary(self):
        """
        Test the send_dictionary function.

        This function tests sending binary and JSON data using the `send_data` function from the `client` module.
        It uses the `patch` context manager to mock user input for choosing between binary and JSON data.

        Raises:
        AssertionError: If the `send_data` function is not called with the expected data.
        """
        
        print('Testing send_dictionary function...')
        # Test then send_dictionary function
        # Test sending binary
        with patch('builtins.input', side_effect=['B']):
            with patch('client.send_data') as mock_send_data:
                app.send_dictionary()
                mock_send_data.assert_called_once_with(result_dict_binary)

        # Test sending JSON
        with patch('builtins.input', side_effect=['J']):
            with patch('client.send_data') as mock_send_data:
                app.send_dictionary()
                mock_send_data.assert_called_once_with(result_dict_json)

    def test_serialize_xml(self):
        """
        Test the serialize_xml function

        This function tests the `serialize_xml ` function from the `client` module.

        Raises:
        AssertionError: If the `serialize_xml` function is not called with the expected data.
        """

        print('Testing serialize_xml function...')
        # Test the serialize_xml function
        self.assertEqual(app.serialize_xml(test_dict), result_dict_xml)

    def test_send_text_file(self):
        """
        Test the send_text_file function.

        This function tests sending a text file using the `send_data` function from the `client` module.
        It uses the `patch` context manager to mock user input for choosing between encrypting the file or not.

        Raises:
        AssertionError: If the `send_data` function is not called with the expected data.
        """

        print('Testing send_text_file function...')
        # Test the send_text_file function
        with patch('builtins.input', side_effect=[test_file, 'N']):
            with patch('client.send_data') as mock_send_data:
                app.send_text_file()
                mock_send_data.assert_called_once_with(result_file1)

        # Cannot test encryption as the the algorythm doees not result in the same value
        # with patch('builtins.input', side_effect=[test_d, 'Y']):
        #     with patch('client.send_data') as mock_send_data:
        #         app.send_text_file()
        #         mock_send_data.assert_called_once_with(result_file2)

    def test_send_exit(self):
        """
        Test the send_exit function.

        This function tests sending the 'EXIT' signal using the `send_data` function from the `client` module.

        AssertionError: If the `send_exit` functions is not called with the expected data.
        """
    
        print('Testing send_exit function...')
        # Test the send_exit function
        with patch('client.send_data') as mock_send_data:
            app.send_exit()
            mock_send_data.assert_called_once_with('EXIT')

if __name__ == '__main__':
    unittest.main()
