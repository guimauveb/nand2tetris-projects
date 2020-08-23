//push constant 7 line 0
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 8 line 1
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
//add line 2
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M+D
M=D
@SP
AM=M+1
//Endless Loop
(END)
@END
0;JMP
