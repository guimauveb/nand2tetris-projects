### Hack assembler ###

# Read the next assembly langage command #

# Create a table containing commands and their opcodes #
label_symbol = ''
symbol_table = {'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 
                'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 
                'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 
                'R13': 13, 'R14': 14, 'R15': 15, 
                'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3,
                'THAT': 4, 'KBD': 24576, 'SCREEN': 16384
                }
binary_lines = []
instruction_counter = 0
variable_value = 16
assembly_file = 'max/Max.asm'
machine_code_file = assembly_file[:-3] + 'hack'

### First pass, count valid lines, store label symbols ###
with open(assembly_file, 'r') as first_pass:

    for checked_line in first_pass:
        checked_line = checked_line.strip()
        label_symbol = ''
        try:
            if checked_line[0] == '/': 
                continue

            elif checked_line[0] == '(':
                for c in checked_line:
                    if c == '(' or c == ')':
                        continue
                    elif c == ' ' or c == '/':
                        break
                    else:
                        label_symbol += c

                symbol_table[label_symbol] = instruction_counter
            else:
                instruction_counter += 1

        except IndexError:
            continue

### Second pass, convert to machine code ###
with open(assembly_file, 'r') as assembly_code, open(machine_code_file, 'w') as machine_code:

    for line in assembly_code:
        binary_code = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        a_binary_string, c_binary_string = '', ''
        dest_bits = ''
        comp_bits = ''
        jump_bits = ''
        cleaned_line = ''
        line = line.strip()

        try:
            if line[0] == '/':
                continue
        except IndexError:
            continue

        for c in line:
            if c == '(' or c == ')':
                continue
            elif c == ' ':
                break
            else:
                cleaned_line += c

        # if A instruction
        if '@' in cleaned_line:
            decimal_address = cleaned_line[1:]
            try:
                if decimal_address in symbol_table.keys():
                    decimal_address = symbol_table[decimal_address]
                else:
                    if not decimal_address.isnumeric():
                        symbol_table[decimal_address] = variable_value
                        decimal_address = symbol_table[decimal_address]
                        variable_value += 1
            except KeyError:
                pass

            decimal_address = int(decimal_address)
            for i in range(15, -1, -1):
                quotient = int(decimal_address / 2 ** i)
                reste = int(decimal_address % 2 ** i)
                decimal_address = reste
                if quotient == 1 and reste == 0:
                    binary_code[i] = 1
                    break
                elif quotient == 1:
                    binary_code[i] = 1
            for b in binary_code[::-1]:
                a_binary_string += str(b)
            if a_binary_string != '':
                binary_lines.append(a_binary_string)
            else:
                continue

        # if C instruction
        elif not '@' in cleaned_line:
            binary_code[0:3] = 1,1,1
            if '=' in line:
                dest_bits = cleaned_line.split('=')[0]
            # dest bits = binary_code[10:13]
                if dest_bits == 'M':
                    binary_code[10:13] = 0,0,1
                elif dest_bits == 'D':
                    binary_code[10:13] = 0,1,0
                elif dest_bits == 'MD':
                    binary_code[10:13] = 0,1,1
                elif dest_bits == 'A':
                    binary_code[10:13] = 1,0,0
                elif dest_bits == 'AM':
                    binary_code[10:13] = 1,0,1
                elif dest_bits == 'AD':
                    binary_code[10:13] = 1,1,0
                elif dest_bits == 'AMD':
                    binary_code[10:13] = 1,1,1

                # comp bits = binary_code[4:10]
                comp_bits = cleaned_line.split('=')[1]
                if comp_bits == '0':
                    binary_code[4:10] = 1,0,1,0,1,0
                elif comp_bits == '1':
                    binary_code[4:10] = 1,1,1,1,1,1
                elif comp_bits == '-1':
                    binary_code[4:10] = 1,1,1,0,1,0
                elif comp_bits == 'D':
                    binary_code[4:10] = 0,0,1,1,0,0
                elif comp_bits == 'A':
                    binary_code[4:10] = 1,1,0,0,0,0
                elif comp_bits == '!D':
                    binary_code[4:10] = 0,0,1,1,0,1
                elif comp_bits == '!A':
                    binary_code[4:10] = 1,1,0,0,0,1
                elif comp_bits == '-D':
                    binary_code[4:10] = 0,0,1,1,1,1
                elif comp_bits == '-A':
                    binary_code[4:10] = 1,1,0,0,1,1
                elif comp_bits == 'D+1':
                    binary_code[4:10] = 0,1,1,1,1,1
                elif comp_bits == 'A+1':
                    binary_code[4:10] = 1,1,0,1,1,1
                elif comp_bits == 'D-1':
                    binary_code[4:10] = 0,0,1,1,1,0
                elif comp_bits == 'A-1':
                    binary_code[4:10] = 1,1,0,0,1,0
                elif comp_bits == 'D+A':
                    binary_code[4:10] = 0,0,0,0,1,0
                elif comp_bits == 'D-A':
                    binary_code[4:10] = 0,1,0,0,1,1
                elif comp_bits == 'A-D':
                    binary_code[4:10] = 0,0,0,1,1,1
                elif comp_bits == 'D&A':
                    binary_code[4:10] = 0,0,0,0,0,0
                elif comp_bits == 'D|A':
                    binary_code[4:10] = 0,1,0,1,0,1

                else:
                    # if M in comp_bits, a = 1
                    binary_code[3] = 1
                    if comp_bits == 'M':
                        binary_code[4:10] = 1,1,0,0,0,0
                    elif comp_bits == '!M':
                        binary_code[4:10] = 1,1,0,0,0,1
                    elif comp_bits == '-M':
                        binary_code[4:10] = 1,1,0,0,1,1
                    elif comp_bits == 'M+1':
                        binary_code[4:10] = 1,1,0,1,1,1
                    elif comp_bits == 'M-1':
                        binary_code[4:10] = 1,1,0,0,1,0
                    elif comp_bits == 'D+M':
                        binary_code[4:10] = 0,0,0,0,1,0
                    elif comp_bits == 'D-M':
                        binary_code[4:10] = 0,1,0,0,1,1
                    elif comp_bits == 'M-D':
                        binary_code[4:10] = 0,0,0,1,1,1
                    elif comp_bits == 'D&M':
                        binary_code[4:10] = 0,0,0,0,0,0
                    elif comp_bits == 'D|M':
                        binary_code[4:10] = 0,1,0,1,0,1


                for b in binary_code:
                    c_binary_string += str(b)
                if c_binary_string != '':
                    binary_lines.append(c_binary_string)
                else:
                    continue

            ### end if '=' in line ###
            elif ';' in cleaned_line:

                comp_bits = cleaned_line.split(';')[0]
                binary_code[3] = 0
                if comp_bits == '0':
                    binary_code[4:10] = 1,0,1,0,1,0
                elif comp_bits == '1':
                    binary_code[4:10] = 1,1,1,1,1,1
                elif comp_bits == '-1':
                    binary_code[4:10] = 1,1,1,0,1,0
                elif comp_bits == 'D':
                    binary_code[4:10] = 0,0,1,1,0,0
                elif comp_bits == 'A':
                    binary_code[4:10] = 1,1,0,0,0,0
                elif comp_bits == '!D':
                    binary_code[4:10] = 0,0,1,1,0,1
                elif comp_bits == '!A':
                    binary_code[4:10] = 1,1,0,0,0,1
                elif comp_bits == '-D':
                    binary_code[4:10] = 0,0,1,1,1,1
                elif comp_bits == '-A':
                    binary_code[4:10] = 1,1,0,0,1,1
                elif comp_bits == 'D+1':
                    binary_code[4:10] = 0,1,1,1,1,1
                elif comp_bits == 'A+1':
                    binary_code[4:10] = 1,1,0,1,1,1
                elif comp_bits == 'D-1':
                    binary_code[4:10] = 0,0,1,1,1,0
                elif comp_bits == 'A-1':
                    binary_code[4:10] = 1,1,0,0,1,0
                elif comp_bits == 'D+A':
                    binary_code[4:10] = 0,0,0,0,1,0
                elif comp_bits == 'D-A':
                    binary_code[4:10] = 0,1,0,0,1,1
                elif comp_bits == 'A-D':
                    binary_code[4:10] = 0,0,0,1,1,1
                elif comp_bits == 'D&A':
                    binary_code[4:10] = 0,0,0,0,0,0
                elif comp_bits == 'D|A':
                    binary_code[4:10] = 0,1,0,1,0,1


                else:
                    binary_code[3] = 1
                    if comp_bits == 'M':
                        binary_code[4:10] = 1,1,0,0,0,0
                    elif comp_bits == '!M':
                        binary_code[4:10] = 1,1,0,0,0,1
                    elif comp_bits == '-M':
                        binary_code[4:10] = 1,1,0,0,1,1
                    elif comp_bits == 'M+1':
                        binary_code[4:10] = 1,1,0,1,1,1
                    elif comp_bits == 'M-1':
                        binary_code[4:10] = 1,1,0,0,1,0
                    elif comp_bits == 'D+M':
                        binary_code[4:10] = 0,0,0,0,1,0
                    elif comp_bits == 'D-M':
                        binary_code[4:10] = 0,1,0,0,1,1
                    elif comp_bits == 'M-D':
                        binary_code[4:10] = 0,0,0,1,1,1
                    elif comp_bits == 'D&M':
                        binary_code[4:10] = 0,0,0,0,0,0
                    elif comp_bits == 'D|M':
                        binary_code[4:10] = 0,1,0,1,0,1

                # jump_bits = binary_code[13:]
                jump_bits = cleaned_line.split(';')[1]
                if jump_bits == 'JGT':
                    binary_code[13:] = 0,0,1
                elif jump_bits == 'JEQ':
                    binary_code[13:] = 0,1,0
                elif jump_bits == 'JGE':
                    binary_code[13:] = 0,1,1
                elif jump_bits == 'JLT':
                    binary_code[13:] = 1,0,0
                elif jump_bits == 'JNE':
                    binary_code[13:] = 1,0,1
                elif jump_bits == 'JLE':
                    binary_code[13:] = 1,1,0
                elif jump_bits == 'JMP':
                    binary_code[13:] = 1,1,1

                for b in binary_code:
                    c_binary_string += str(b)

                if c_binary_string != '':
                    binary_lines.append(c_binary_string)
                else:
                    continue

            ### end if ';' in line ###     
               
    for l in binary_lines:
        print(l, file=machine_code)
        