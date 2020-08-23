def c_push(segment, i, assembly_code, vm_instruction, filename):

    if segment == 'constant':

        command_lines = [
                        '@' + str(i),
                        'D=A',
                        '@SP',
                        'A=M',
                        'M=D',
                        '@SP',
                        'M=M+1'
                        ]
        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

### À GROUPER ###

    elif segment == 'local':

        command_lines = [
                        '@LCL',
                        'D=M',
                        '@' + str(i), 
                        'A=A+D', 
                        'D=M', 
                        '@SP',
                        'A=M', 
                        'M=D', 
                        '@SP',
                        'M=M+1', 
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

    elif segment == 'argument':

        command_lines = [
                        '@ARG',
                        'D=M',
                        '@' + str(i),
                        'A=A+D', 
                        'D=M', 
                        '@SP',
                        'A=M',
                        'M=D',
                        '@SP',
                        'M=M+1', 
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

    elif segment == 'this':

        command_lines = [
                        '@THIS',
                        'D=M',
                        '@' + str(i), 
                        'A=A+D', 
                        'D=M',
                        '@SP',
                        'A=M', 
                        'M=D',
                        '@SP',
                        'M=M+1',
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

    elif segment == 'that':

        command_lines = [
                        '@THAT',
                        'D=M',
                        '@' + str(i),
                        'A=A+D',
                        'D=M',
                        '@SP',
                        'A=M',
                        'M=D',
                        '@SP',
                        'M=M+1',
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

### FIN À GROUPER ###

    elif segment == 'static':

        static_variable = list(filename.split('/'))[-1][:-3]
        command_lines = [
                        '@' + static_variable + str(i),
                        'D=M', 
                        '@SP',
                        'A=M', 
                        'M=D',
                        '@SP',
                        'M=M+1',
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

    elif segment == 'temp':

        i += 5
        command_lines = [
                        '@' + str(i),
                        'D=M',
                        '@SP',
                        'A=M', 
                        'M=D', 
                        '@SP',
                        'M=M+1', 
                        ]
        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

    elif segment == 'pointer':

        if i == 0:
            command_lines = [       
                            '@THIS',
                            'D=M',
                            '@SP',
                            'A=M',
                            'M=D',
                            '@SP',
                            'M=M+1'
                            ]
        elif i == 1:
            command_lines = [       
                            '@THAT',
                            'D=M', 
                            '@SP',
                            'A=M', 
                            'M=D', 
                            '@SP',
                            'M=M+1',
                            ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]


def c_pop(segment, i, assembly_code, vm_instruction, filename):

#### À GROUPER ###

    if segment == 'local':
        command_lines = [
                        '@LCL',
                        'D=M', 
                        '@' + str(i),
                        'D=D+A',
                        '@R13',
                        'M=D',
                        '@SP',
                        'AM=M-1',
                        'D=M',
                        '@R13',
                        'A=M',
                        'M=D'
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

    elif segment == 'argument':
        command_lines = [
                        '@ARG',
                        'D=M', 
                        '@' + str(i),
                        'D=D+A',
                        '@R13',
                        'M=D',
                        '@SP',
                        'AM=M-1',
                        'D=M',
                        '@R13',
                        'A=M',
                        'M=D',
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

    elif segment == 'this':
        command_lines = [
                        '@THIS',
                        'D=M',
                        '@' + str(i),
                        'D=D+A',
                        '@R13',
                        'M=D',
                        '@SP',
                        'AM=M-1',
                        'D=M',
                        '@R13',
                        'A=M', 
                        'M=D',
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

    elif segment == 'that':
        command_lines = [
                        '@THAT',
                        'D=M', 
                        '@' + str(i),
                        'D=D+A',
                        '@R13',
                        'M=D',
                        '@SP',
                        'AM=M-1',
                        'D=M',
                        '@R13',
                        'A=M', 
                        'M=D'
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

#### FIN À GROUPER ###

    elif segment == 'static':

        static_variable = list(filename.split('/'))[-1][:-3]
        command_lines = [
                        '@SP',
                        'AM=M-1',
                        'D=M',
                        '@' + static_variable + str(i),
                        'M=D',
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

    elif segment == 'temp':

        i += 5

        command_lines = [
                        '@' + str(i),
                        'D=A',
                        '@R13',
                        'M=D',
                        '@SP',
                        'AM=M-1',
                        'D=M',
                        '@R13',
                        'A=M',
                        'M=D'
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

    elif segment == 'pointer':
        if i == 0:
            command_lines = [
                        '@SP',
                        'AM=M-1',
                        'D=M',
                        '@THIS',
                        'M=D',
                        ]

        elif i == 1:
            command_lines = [
                        '@SP',
                        'AM=M-1',
                        'D=M', 
                        '@THAT',
                        'M=D',
                        ]

        assembly_code[vm_instruction] = [cmd for cmd in command_lines]

