def bootstrap():
    function_name = 'Sys.init'
    return_address = function_name + 'ret$0'
    command_lines = [
                    ### set sp
                    '@256',
                    'D=A',
                    '@SP',
                    'M=D',
                    ### push the return address ###
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
                    '@0',
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

