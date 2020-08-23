import os
import random
from bootstrap import bootstrap
from arithmetic import writeAdd, writeSub, writeNeg, writeEq, writeGt
from arithmetic import writeLt, writeAnd, writeOr, writeNot
from pushpop import writePush, writePop
from branching import writeLabel, writeIf, writeGoto
from function import writeCall, writeFunction, writeReturn

dispatcher = {'bootstrap': bootstrap, 
              'arithmetic': {'add': writeAdd, 'sub': writeSub, 'neg': writeNeg,
                             'eq': writeEq, 'gt': writeGt, 'lt': writeLt,
                             'and': writeAnd, 'or': writeOr, 'not': writeNot}, 
              'push/pop': {'push': writePush, 'pop': writePop},
              'branching': {'label': writeLabel, 'if-goto': writeIf, 'goto': writeGoto},
              'function': {'call': writeCall, 'function': writeFunction, 
              'return': writeReturn}
              }
assembly_code = {}

def codewriter(input_path, vm_code, bootstrap, output_path):
    filename = output_path[-1]
    if bootstrap == True:
        assembly_code['//bootstrap'] = [cmd for cmd in 
                                    dispatcher['bootstrap']()]
    else:
        pass
    line_number = 0
    for file, lines in zip(vm_code, vm_code.values()):

        for line in lines:
            vm_instruction = '//' + line + ' line ' + str(line_number)
            line = line.split(' ')
            if line[0] in dispatcher['push/pop']:
              assembly_code[vm_instruction] = [cmd for cmd in 
                                                dispatcher['push/pop'][line[0]](
                                                                segment=line[1], 
                                                                i=int(line[2]),
                                                                filename=file,
                                                                line_number=str(line_number)
                                                                )
                                                ]
            elif line[0] in dispatcher['arithmetic']:
              assembly_code[vm_instruction] = [cmd for cmd in 
                                                dispatcher['arithmetic'][line[0]](
                                                                line_number=str(line_number)
                                                                )
                                                ]
            elif line[0] in dispatcher['branching']:
              assembly_code[vm_instruction] = [cmd for cmd in 
                                                dispatcher['branching'][line[0]](
                                                                label=line[1]
                                                                )
                                                ]
            elif line[0] in dispatcher['function']:
                if line[0] == 'call':
                    assembly_code[vm_instruction] = [cmd for cmd in 
                                                  dispatcher['function'][line[0]](
                                                                line_number=str(line_number),
                                                                filename=filename,
                                                                function_name=line[1],
                                                                nArgs=line[2]  
                                                                )
                                                ]
                elif line[0] == 'function':
                    assembly_code[vm_instruction] = [cmd for cmd in 
                                                  dispatcher['function'][line[0]](
                                                                filename=filename,
                                                                function_name=line[1],
                                                                nVars=line[2]
                                                                )
                                                  ]
                elif line[0] == 'return':
                    assembly_code[vm_instruction] = [cmd for cmd in 
                                                  dispatcher['function'][line[0]](
                                                                line_number=str(line_number)
                                                                )
                                                  ]
            line_number += 1

    output_file = os.path.join(*output_path, output_path[-1] + '.asm')
    with open(output_file, 'w') as output:
        assembly_code['//Endless Loop'] = ['(END)', '@END', '0;JMP']
        for key, value in zip(assembly_code.keys(), assembly_code.values()):
            print(key, file=output)
            for line in value:
                print(line, file=output)
    return print(f"'{filename}.vm' successfully compiled to Assembly code.")

