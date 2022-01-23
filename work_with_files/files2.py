#!/usr/bin/env python
# coding: utf-8
    
    def write_array(array, file_name):
        """записывает строки из array в файл file_name"""
        with open(file_name, 'a') as file:
            file.writelines(array)
    
    with open('text1.txt', 'w') as file:
        file.writelines([' line1  \n', '   line2\n', '\n', 'line3\n line4 \nline5 \nline6'])
        
    with open('text1.txt', 'r') as file:
        lines = file.readlines() # - список строк
        
    write_array(lines, 'output.txt')    
