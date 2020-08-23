//push constant 0 line 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 0          line 1
@LCL
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//label LOOP_START line 2
@LOOP_START
//push argument 0 line 3
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 0 line 4
@LCL
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//add line 5
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
AM=M+1
//pop local 0	         line 6
@LCL
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//push argument 0 line 7
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1 line 8
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub line 9
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
AM=M+1
//pop argument 0       line 10
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//push argument 0 line 11
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//if-goto LOOP_START   line 12
@SP
AM=M-1
D=M
@LOOP_START
D;JNE
//push local 0 line 13
@LCL
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//Endless Loop
(END)
@END
0;JMP
