""" 

Author: Dillon Mantle
Date: 2023-07-28
"""


# Baseline Test data
test_dict = {'Developer': 'Dillon', 'Tester': 'Lester', 'ProjectManager': 'Yasmin'}
test_file = 'test file content'

# Expected results for various phases of the process
result_dict_binary = 'DICT:BINARY:\x80\x04\x95F\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\tDeveloper\x94\x8c\x06Dillon\x94\x8c\x06Tester\x94\x8c\x06Lester\x94\x8c\x0eProjectManager\x94\x8c\x06Yasmin\x94u.'
result_binary = 'BINARY:\x80\x04\x95F\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\tDeveloper\x94\x8c\x06Dillon\x94\x8c\x06Tester\x94\x8c\x06Lester\x94\x8c\x0eProjectManager\x94\x8c\x06Yasmin\x94u.'
result_dict_json = 'DICT:JSON:{"Developer": "Dillon", "Tester": "Lester", "ProjectManager": "Yasmin"}'
result_json = 'JSON:{"Developer": "Dillon", "Tester": "Lester", "ProjectManager": "Yasmin"}'
result_dict_xml = '<dictionary><Developer>Dillon</Developer><Tester>Lester</Tester><ProjectManager>Yasmin</ProjectManager></dictionary>'
result_file1 = 'FILE:test file content'
result_file2 = 'FILE:ENCRYPTEDgAAAAABkw-BE_zMOWNPmZ9TXLF12MyNSo7m5leKstmSnpa3zlKiRjVri3uU4qEo2Ok89YMmeqJ5WuTWNRI5fapJ7leoQTKsnIA=='











# Server test cases
test_e = 'BINARY:\x80\x04\x95G\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\tDeveloper\x94\x8c\x06Dillon\x94\x8c\x06Tester\x94\x8c\x06Lester\x94\x8c\x0fProject manager\x94\x8c\x06Yasmin\x94u.'
result_e = {'Developer': 'Dillon', 'Tester': 'Lester', 'Project manager': 'Yasmin'}

# Save dictionary
test_f = 'BINARY:G}(     DeveloperDillonTesterLesterProject managerYasminu.'
result_f = {'Developer': 'Dillon', 'Tester': 'Lester', 'Project manager': 'Yasmin'}

# Test XML
test_g = '<dictionary><Developer>Dillon</Developer><Tester>Lester</Tester><Project manager>Yasmin</Project manager></dictionary>'
result_g = {'Developer': 'Dillon', 'Tester': 'Lester', 'Project manager': 'Yasmin'}

