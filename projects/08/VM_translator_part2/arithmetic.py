def writeAdd(line_number):
    command_lines = [
                    '@SP',
                    'AM=M-1',
                    'D=M',
                    '@SP',
                    'AM=M-1',
                    'M=M+D',
                    '@SP',
                    'AM=M+1',
                    ]
    return command_lines

def writeSub(line_number):
    command_lines = [
                    '@SP',
                    'AM=M-1',
                    'D=M',
                    '@SP',
                    'AM=M-1',
                    'M=M-D',
                    '@SP',
                    'AM=M+1',
                    ]
    return command_lines

def writeNeg(line_number):
    command_lines = [
                    '@SP',
                    'AM=M-1',
                    'M=-M',
                    '@SP',
                    'AM=M+1'
                    ]
    return command_lines

def writeEq(line_number):
    command_lines = [
                    '@SP',
                    'AM=M-1',
                    'D=M',
                    '@SP',
                    'AM=M-1',
                    'D=M-D',
                    '@ISEQUAL' + line_number,
                    'D;JEQ',
                    '@ISNOTEQUAL' + line_number,
                    'D;JNE',
                    '(ISEQUAL' + line_number + ')',
                    '@SP',
                    'A=M',
                    'M=-1',
                    '@SP',
                    'M=M+1',
                    '@END' + line_number,
                    '0;JMP',
                    '(ISNOTEQUAL' + line_number + ')',
                    '@SP',
                    'A=M',
                    'M=0',
                    '@SP',
                    'M=M+1',
                    '(END' + line_number + ')',
                    ]
    return command_lines

def writeGt(line_number):
    command_lines = [
                    '@SP',
                    'AM=M-1',
                    'D=M',
                    '@SP',
                    'AM=M-1',
                    'D=M-D',
                    '@ISGREATER' + line_number,
                    'D;JGT',
                    '@ISNOTGREATER' + line_number,
                    'D;JLE',
                    '(ISGREATER' + line_number + ')',
                    '@SP',
                    'A=M',
                    'M=-1',
                    '@SP',
                    'M=M+1',
                    '@END' + line_number,
                    '0;JMP',
                    '(ISNOTGREATER' + line_number + ')',
                    '@SP',
                    'A=M',
                    'M=0',
                    '@SP',
                    'M=M+1',
                    '(END' + line_number + ')',
                    ]  
    return command_lines

def writeLt(line_number):
    command_lines = [
                    '@SP',
                    'AM=M-1',
                    'D=M',
                    '@SP',
                    'AM=M-1',
                    'D=M-D',
                    '@ISLESS' + line_number,
                    'D;JLT',
                    '@ISNOTLESS' + line_number,
                    'D;JGE',
                    '(ISLESS' + line_number + ')',
                    '@SP',
                    'A=M',
                    'M=-1',
                    '@SP',
                    'M=M+1',
                    '@END' + line_number,
                    '0;JMP',
                    '(ISNOTLESS' + line_number + ')',
                    '@SP',
                    'A=M',
                    'M=0',
                    '@SP',
                    'M=M+1',
                    '(END' + line_number + ')',
                    ]
    return command_lines

def writeAnd(line_number):
    command_lines = [
                    '@SP',
                    'AM=M-1',
                    'D=M',
                    '@SP',
                    'AM=M-1',
                    'D=D&M',
                    '@SP',
                    'A=M',
                    'M=D',
                    '@SP',
                    'AM=M+1'
                    ]
    return command_lines

def writeOr(line_number):
    command_lines = [
                    '@SP',
                    'AM=M-1',
                    'D=M',
                    '@SP',
                    'AM=M-1',
                    'D=D|M',
                    '@SP',
                    'A=M',
                    'M=D',
                    '@SP',
                    'AM=M+1'
                    ]
    return command_lines

def writeNot(line_number):
    command_lines = [
                    '@SP',
                    'AM=M-1',
                    'M=!M',
                    '@SP',
                    'AM=M+1'
                    ]
    return command_lines
