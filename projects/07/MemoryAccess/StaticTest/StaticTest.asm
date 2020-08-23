//push constant 111 line 0
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 333 line 1
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 888 line 2
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop static 8 line 3
@SP
M=M-1
A=M
D=M
@StaticTest8
M=D
//pop static 3 line 4
@SP
M=M-1
A=M
D=M
@StaticTest3
M=D
//pop static 1 line 5
@SP
M=M-1
A=M
D=M
@StaticTest1
M=D
//push static 3 line 6
@StaticTest3
D=M
@SP
A=M
M=D
@SP
M=M+1
//push static 1 line 7
@StaticTest1
D=M
@SP
A=M
M=D
@SP
M=M+1
//sub line 8
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
M=D
@SP
AM=M+1
//push static 8 line 9
@StaticTest8
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
D=M+D
M=D
@SP
AM=M+1
//Endless Loop
(END)
@END
0;JMP
