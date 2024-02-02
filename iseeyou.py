import sys

def check_spaces_and_tabs(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            ascii_string = ''
            for char in line:
                if char == ' ':
                    ascii_string += '1'
                elif char == '\t':
                    ascii_string += '0'
                    
            # Split the binary string into chunks of 8 digits
            chunks = [ascii_string[i:i+8] for i in range(0, len(ascii_string), 8)]

            # Convert each chunk to its ASCII form and join them
            ascii_output = ''.join([chr(int(chunk, 2)) for chunk in chunks])

            print(ascii_output, end='')

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print("Usage: python iseeyou.py <file_path>")
        print("Options:")
        print("  -h, --help       Show this help message and exit")
        sys.exit(1)
    file_path = sys.argv[1]
    check_spaces_and_tabs(file_path)
