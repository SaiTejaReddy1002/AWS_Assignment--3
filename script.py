import pathlib
import socket
from collections import Counter

# Paths to the directories
data_dir = pathlib.Path('/home/data')
output_dir = pathlib.Path('/home/output')

# Files to process
file_list = ['IF.txt', 'Limerick-1.txt']

# Store word counts per file
counts_per_file = {}

# Variable for the aggregate word count
aggregate_words = 0

# Process each file to count words
for file_name in file_list:
    file_path = data_dir / file_name
    with file_path.open('r') as file_content:
        word_list = file_content.read().split()
        counts_per_file[file_name] = len(word_list)
        aggregate_words += len(word_list)

# Obtain the IP address of the current machine
current_ip = socket.gethostbyname(socket.gethostname())

# Output file path
result_file_path = output_dir / 'result.txt'

# Writing the counts and IP address to the output file
with result_file_path.open('w') as output_file:
    for file_name, word_count in counts_per_file.items():
        output_file.write(f"{file_name}: {word_count} words\n")
    output_file.write(f"Total word count: {aggregate_words}\n")
    output_file.write(f"Machine IP: {current_ip}\n")

# Displaying the content of the output file
with result_file_path.open('r') as output_file:
    print(output_file.read())
