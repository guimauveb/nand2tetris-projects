def writeLabel(label):
    command_lines = [
                     '(' + label + ')',
                     ]
    return command_lines

def writeIf(label):
    command_lines = [
                     '@SP',
                     'AM=M-1',
                     'D=M',
                     '@' + label, 
                     'D;JNE',
                    ]
    return command_lines

def writeGoto(label):
    command_lines = [
                     '@' + label,
                     '0;JMP',
                    ]
    return command_lines

