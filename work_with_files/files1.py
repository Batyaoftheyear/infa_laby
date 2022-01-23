#!/usr/bin/env python
# coding: utf-8

with open('text1.txt', 'w') as file:
    file.writelines([' line1  \n', '   line2\n', '\n', 'line3\n line4 \nline 5 \nline6'])
    
with open('text1.txt', 'r') as file:
    lines = [line.strip() for line in file]
    print('\n'.join(lines))
