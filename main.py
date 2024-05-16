import os
print(os.getcwd())
import re
with open('matrix.txt', 'r') as file:
    lines = file.readlines()
n, m = map(int, lines[0].split())
matrix = [line.strip() for line in lines[1:]]
decoded_string = ''.join([''.join(row) for row in zip(*matrix)])
cleaned_string = re.sub(r'[^a-zA-Z0-9]+', ' ', decoded_string)
print(cleaned_string)
