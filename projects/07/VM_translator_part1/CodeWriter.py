import os
import random
from arithmetic import add, sub, neg, eq, gt, lt, and_command, or_command, not_command
from pushpop import c_push, c_pop

dispatcher = {'add': add, 'sub': sub, 'neg': neg,
              'eq': eq, 'gt': gt, 'lt': lt, 
              'and': and_command, 'or': or_command, 
              'not': not_command, 'push': c_push, 'pop': c_pop
              }
command_lines = {''}
assembly_code = {}

def codewriter(filename, vm_code):

    for line, i in zip(vm_code, range(len(vm_code))):
        vm_instruction = '//' + line + ' line ' + str(i)
        line = line.split(' ')

        ### if push/pop command ###
        if len(line) > 1:
           dispatcher[line[0]](line[1], int(line[2]), assembly_code, vm_instruction, filename)

        ### if arithmetic command ###
        elif len(line) == 1:
            assembly_code[vm_instruction] = [cmd for cmd in dispatcher[line[0]](str(i))]

    filepath = filename[:-3] + '.asm'
    with open(filepath, 'w') as output:
        assembly_code['//Endless Loop'] = ['(END)', '@END', '0;JMP']

        for key, value in zip(assembly_code.keys(), assembly_code.values()):
            print(key, file=output)

            for line in value:
                print(line, file=output)

    return print(f"'{filename}' successfully compiled to Assembly code.")

