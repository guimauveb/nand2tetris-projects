def parser(filename):

    with open(filename, 'r') as input_file:
        to_convert = []
        
        for line in input_file:
            cleaned_line = ''
            line = line.split('\n')
            line = line[0].strip()

            try:
                if line[0] == '/':
                    continue
            except IndexError:
                continue
                
            for c in line:
                if c == '/':
                    break
                else:
                    cleaned_line += c
            to_convert.append(cleaned_line)

    return to_convert
