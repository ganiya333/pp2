with open (r'text_file.txt', 'r') as file:
    num_of_lines=len(file.readlines())
    print(num_of_lines)