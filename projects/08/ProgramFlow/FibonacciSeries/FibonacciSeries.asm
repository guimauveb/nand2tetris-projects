//push argument 1 line 0
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1            line 1
@SP
AM=M-1
D=M
@THAT
M=D
//push constant 0 line 2
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 0               line 3
@THAT
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
//push constant 1 line 4
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 1               line 5
@THAT
D=M
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//push argument 0 line 6
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2 line 7
@2
D=A
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
M=M-D
@SP
AM=M+1
//pop argument 0           line 9
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
//label MAIN_LOOP_START line 10
(MAIN_LOOP_START)
//push argument 0 line 11
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//if-goto COMPUTE_ELEMENT  line 12
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JNE
//goto END_PROGRAM         line 13
@END_PROGRAM
0;JMP
//label COMPUTE_ELEMENT line 14
(COMPUTE_ELEMENT)
//push that 0 line 15
@THAT
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//push that 1 line 16
@THAT
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//add line 17
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
AM=M+1
//pop that 2               line 18
@THAT
D=M
@2
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//push pointer 1 line 19
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1 line 20
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//add line 21
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
AM=M+1
//pop pointer 1            line 22
@SP
AM=M-1
D=M
@THAT
M=D
//push argument 0 line 23
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1 line 24
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub line 25
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
AM=M+1
//pop argument 0           line 26
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
//goto MAIN_LOOP_START line 27
@MAIN_LOOP_START
0;JMP
//label END_PROGRAM line 28
(END_PROGRAM)
//Endless Loop
(END)
@END
0;JMP
