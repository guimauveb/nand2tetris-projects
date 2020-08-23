
def writePush(segment, i, filename, line_number):
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
        return command_lines

### À GROUPER, créer dic ###
    elif segment == 'local':
        command_lines = [
                        '@LCL',
                        'D=M',
                        '@' + str(i), 
                        'A=D+A', 
                        'D=M', 
                        '@SP',
                        'A=M', 
                        'M=D', 
                        '@SP',
                        'M=M+1', 
                        ]
        return command_lines

    elif segment == 'argument':
        command_lines = [
                        '@ARG',
                        'D=M',
                        '@' + str(i),
                        'A=D+A', 
                        'D=M', 
                        '@SP',
                        'A=M',
                        'M=D',
                        '@SP',
                        'M=M+1', 
                        ]
        return command_lines

    elif segment == 'this':
        command_lines = [
                        '@THIS',
                        'D=M',
                        '@' + str(i), 
                        'A=D+A', 
                        'D=M',
                        '@SP',
                        'A=M', 
                        'M=D',
                        '@SP',
                        'M=M+1',
                        ]
        return command_lines

    elif segment == 'that':
        command_lines = [
                        '@THAT',
                        'D=M',
                        '@' + str(i),
                        'A=D+A',
                        'D=M',
                        '@SP',
                        'A=M',
                        'M=D',
                        '@SP',
                        'M=M+1',
                        ]
        return command_lines
### FIN À GROUPER ###

    elif segment == 'static':
        static_variable = filename[:-2] + str(i)
        command_lines = [
                        '@' + static_variable,
                        'D=M', 
                        '@SP',
                        'A=M', 
                        'M=D',
                        '@SP',
                        'M=M+1',
                        ]
        return command_lines

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
        return command_lines

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
        return command_lines


def writePop(segment, i, filename, line_number):
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
        return command_lines

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
        return command_lines

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
        return command_lines

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
        return command_lines
#### FIN À GROUPER ###

    elif segment == 'static':
        static_variable = filename[:-2] + str(i)
        command_lines = [
                        '@SP',
                        'AM=M-1',
                        'D=M',
                        '@' + static_variable,
                        'M=D',
                        ]
        return command_lines

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
        return command_lines

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
        return command_lines

