def writeCall(filename, function_name, nArgs, line_number):
    return_address = function_name + '.$ret.' + line_number
    command_lines = [
                    '@' + return_address,
                    'D=A',
                    '@SP',
                    'A=M',
                    'M=D',
                    '@SP',
                    'M=M+1',

                     ### save the caller frame ###
                     '@LCL',
                     'D=M',
                     '@SP',
                     'A=M',
                     'M=D', ## push LCL
                     '@SP',
                     'M=M+1',
                     '@ARG',
                     'D=M',
                     '@SP',
                     'A=M',
                     'M=D', ## push ARG
                     '@SP',
                     'M=M+1',
                     '@THIS',
                     'D=M',
                     '@SP',
                     'A=M',
                     'M=D', ## push THIS
                     '@SP',
                     'M=M+1',
                     '@THAT',
                     'D=M',
                     '@SP',
                     'A=M',
                     'M=D', ## push THAT
                     '@SP',
                     'M=M+1',

                     ### set ARG pointer ###
                     '@5',
                     'D=A',
                     '@' + nArgs,
                     'D=D+A',
                     '@SP',
                     'D=M-D',   ### D = SP - 5 - nArgs
                     '@ARG',
                     'M=D',

                     ### LCL = SP
                     '@SP',
                     'D=M',
                     '@LCL',
                     'M=D',



                     ### goto 'function'
                     '@' + function_name,
                     '0;JMP',

                     ### declares a label for the return address
                     '(' + return_address + ')',
                     ]
    return command_lines

def writeFunction(filename, function_name, nVars):
    command_lines = [
                    '(' + function_name + ')',
                    '@' + nVars,
                    'D=A',
                    '@R15',
                    'M=D',  ### R15 = counter
                    #### nvars times
                    '@stop.push.nVars.' + function_name,
                    'D;JEQ',    ### don't push args if nvars == 0
                    '(push.nVars.' + function_name + ')',
                    '@SP',
                    'A=M',
                    'M=0',
                    '@SP',
                    'M=M+1',
                    '@R15',
                    'MD=M-1',
                    '@push.nVars.' + function_name,
                    'D;JGT',    ### keep pushing 0's 
                    '(stop.push.nVars.' + function_name + ')'
                    ]
    return command_lines

def writeReturn(line_number):
    command_lines = [

                    '@LCL',
                    'D=M',
                    '@R13',
                    'M=D',
                    '@5',
                    'D=D-A', ### D = R13(endframe) - 5
                    'A=D',
                    'D=M',  ### D = *(R13 - 5)
                    '@retAddr' + line_number,
                    'M=D', ### R14 = *(R13 - 5) = return address

                    '@SP',
                    'AM=M-1',
                    'D=M',
                    '@ARG',
                    'A=M',
                    'M=D',  ## *ARG(310) = return value

                    ### reposition sp for the caller
                    '@ARG',
                    'D=M',
                    '@SP',
                    'M=D+1', ## SP = ARG + 1


                    '@R13',
                    'AM=M-1',
                    'D=M',
                    '@THAT',
                    'M=D',
                    '@R13',
                    'AM=M-1',
                    'D=M',
                    '@THIS',
                    'M=D',
                    '@R13',
                    'AM=M-1',
                    'D=M',
                    '@ARG',
                    'M=D',
                    '@R13',
                    'AM=M-1',
                    'D=M',
                    '@LCL',
                    'M=D',

                    ### return address ###
                    '@retAddr' + line_number,
                    'A=M',
                    '0;JMP'

                    ]
    return command_lines
    