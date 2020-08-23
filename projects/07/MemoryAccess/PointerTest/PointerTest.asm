//push constant 3030 line 0
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0 line 1
@SP
M=M-1
A=M
D=M
@THIS
M=D
//push constant 3040 line 2
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1 line 3
@SP
M=M-1
A=M
D=M
@THAT
M=D
//push constant 32 line 4
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop this 2 line 5
@THIS
D=M
@2
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
//push constant 46 line 6
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 6 line 7
@THAT
D=M
@6
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//push pointer 0 line 8
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push pointer 1 line 9
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//add line 10
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
AM=M+1
//push this 2 line 11
@THIS
D=M
@2
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//sub line 12
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
AM=M+1
//push that 6 line 13
@THAT
D=M
@6
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//add line 14
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
AM=M+1
//Endless Loop
(END)
@END
0;JMP
