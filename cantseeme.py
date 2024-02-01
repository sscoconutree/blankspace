import sys

def convert_ascii_to_binary(file_path):
    binary_output = ''
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                binary_char = format(ord(char), '08b')  # Convert char to 8-bit binary
                binary_output += binary_char + ' '  # Add space between characters
    return binary_output

def replace_binary(binary_string):
    replaced_string = ''
    for bit in binary_string:
        if bit == '1':
            replaced_string += ' '
        elif bit == '0':
            replaced_string += '\t'
    return replaced_string

def write_output(output_text, output_file):
    with open(output_file, 'w') as file:
        file.write(output_text)

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print("Usage: python cantseeme.py <input_file_path> <output_file_path>")
        print("Options:")
        print("  -h, --help       Show this help message and exit")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    binary_output = convert_ascii_to_binary(input_file_path)
    replaced_output = replace_binary(binary_output)
    write_output(replaced_output, output_file_path)
