//push constant 17 line 0
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17 line 1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq line 2
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@ISEQUAL2
D;JEQ
@ISNOTEQUAL2
D;JNE
(ISEQUAL2)
@SP
A=M
M=-1
@SP
M=M+1
@END2
0;JMP
(ISNOTEQUAL2)
@SP
A=M
M=0
@SP
M=M+1
(END2)
//push constant 17 line 3
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 16 line 4
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq line 5
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@ISEQUAL5
D;JEQ
@ISNOTEQUAL5
D;JNE
(ISEQUAL5)
@SP
A=M
M=-1
@SP
M=M+1
@END5
0;JMP
(ISNOTEQUAL5)
@SP
A=M
M=0
@SP
M=M+1
(END5)
//push constant 16 line 6
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17 line 7
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq line 8
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@ISEQUAL8
D;JEQ
@ISNOTEQUAL8
D;JNE
(ISEQUAL8)
@SP
A=M
M=-1
@SP
M=M+1
@END8
0;JMP
(ISNOTEQUAL8)
@SP
A=M
M=0
@SP
M=M+1
(END8)
//push constant 892 line 9
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891 line 10
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt line 11
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@ISLESS11
D;JLT
@ISNOTLESS11
D;JGE
(ISLESS11)
@SP
A=M
M=-1
@SP
M=M+1
@END11
0;JMP
(ISNOTLESS11)
@SP
A=M
M=0
@SP
M=M+1
(END11)
//push constant 891 line 12
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 892 line 13
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt line 14
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@ISLESS14
D;JLT
@ISNOTLESS14
D;JGE
(ISLESS14)
@SP
A=M
M=-1
@SP
M=M+1
@END14
0;JMP
(ISNOTLESS14)
@SP
A=M
M=0
@SP
M=M+1
(END14)
//push constant 891 line 15
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891 line 16
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt line 17
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@ISLESS17
D;JLT
@ISNOTLESS17
D;JGE
(ISLESS17)
@SP
A=M
M=-1
@SP
M=M+1
@END17
0;JMP
(ISNOTLESS17)
@SP
A=M
M=0
@SP
M=M+1
(END17)
//push constant 32767 line 18
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766 line 19
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt line 20
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@ISGREATER20
D;JGT
@ISNOTGREATER20
D;JLE
(ISGREATER20)
@SP
A=M
M=-1
@SP
M=M+1
@END20
0;JMP
(ISNOTGREATER20)
@SP
A=M
M=0
@SP
M=M+1
(END20)
//push constant 32766 line 21
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32767 line 22
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt line 23
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@ISGREATER23
D;JGT
@ISNOTGREATER23
D;JLE
(ISGREATER23)
@SP
A=M
M=-1
@SP
M=M+1
@END23
0;JMP
(ISNOTGREATER23)
@SP
A=M
M=0
@SP
M=M+1
(END23)
//push constant 32766 line 24
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766 line 25
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt line 26
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@ISGREATER26
D;JGT
@ISNOTGREATER26
D;JLE
(ISGREATER26)
@SP
A=M
M=-1
@SP
M=M+1
@END26
0;JMP
(ISNOTGREATER26)
@SP
A=M
M=0
@SP
M=M+1
(END26)
//push constant 57 line 27
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 31 line 28
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 53 line 29
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
//add line 30
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
AM=M+1
//push constant 112 line 31
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub line 32
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
AM=M+1
//neg line 33
@SP
AM=M-1
M=-M
@SP
AM=M+1
//and line 34
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D&M
@SP
A=M
M=D
@SP
AM=M+1
//push constant 82 line 35
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//or line 36
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D|M
@SP
A=M
M=D
@SP
AM=M+1
//not line 37
@SP
AM=M-1
M=!M
@SP
AM=M+1
//Endless Loop
(END)
@END
0;JMP
