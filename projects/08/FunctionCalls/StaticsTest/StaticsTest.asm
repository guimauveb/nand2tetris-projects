//bootstrap
@256
D=A
@SP
M=D
@Sys.initret$0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.initret$0)
//function Sys.init 0 line 0
(Sys.init)
@0
D=A
@R15
M=D
@stop.push.nVars.Sys.init
D;JEQ
(push.nVars.Sys.init)
@SP
A=M
M=0
@SP
M=M+1
@R15
MD=M-1
@push.nVars.Sys.init
D;JGT
(stop.push.nVars.Sys.init)
//push constant 6 line 1
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 8 line 2
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
//call Class1.set 2 line 3
@Class1.set.$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@2
D=D+A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Class1.set.$ret.3)
//pop temp 0  line 4
@5
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//push constant 23 line 5
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 15 line 6
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
//call Class2.set 2 line 7
@Class2.set.$ret.7
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@2
D=D+A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Class2.set.$ret.7)
//pop temp 0  line 8
@5
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//call Class1.get 0 line 9
@Class1.get.$ret.9
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.get
0;JMP
(Class1.get.$ret.9)
//call Class2.get 0 line 10
@Class2.get.$ret.10
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.get
0;JMP
(Class2.get.$ret.10)
//label WHILE line 11
(WHILE)
//goto WHILE line 12
@WHILE
0;JMP
//function Class1.set 0 line 13
(Class1.set)
@0
D=A
@R15
M=D
@stop.push.nVars.Class1.set
D;JEQ
(push.nVars.Class1.set)
@SP
A=M
M=0
@SP
M=M+1
@R15
MD=M-1
@push.nVars.Class1.set
D;JGT
(stop.push.nVars.Class1.set)
//push argument 0 line 14
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
//pop static 0 line 15
@SP
AM=M-1
D=M
@Class1.0
M=D
//push argument 1 line 16
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
//pop static 1 line 17
@SP
AM=M-1
D=M
@Class1.1
M=D
//push constant 0 line 18
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//return line 19
@LCL
D=M
@R13
M=D
@5
D=D-A
A=D
D=M
@retAddr19
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@retAddr19
A=M
0;JMP
//function Class1.get 0 line 20
(Class1.get)
@0
D=A
@R15
M=D
@stop.push.nVars.Class1.get
D;JEQ
(push.nVars.Class1.get)
@SP
A=M
M=0
@SP
M=M+1
@R15
MD=M-1
@push.nVars.Class1.get
D;JGT
(stop.push.nVars.Class1.get)
//push static 0 line 21
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
//push static 1 line 22
@Class1.1
D=M
@SP
A=M
M=D
@SP
M=M+1
//sub line 23
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
AM=M+1
//return line 24
@LCL
D=M
@R13
M=D
@5
D=D-A
A=D
D=M
@retAddr24
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@retAddr24
A=M
0;JMP
//function Class2.set 0 line 25
(Class2.set)
@0
D=A
@R15
M=D
@stop.push.nVars.Class2.set
D;JEQ
(push.nVars.Class2.set)
@SP
A=M
M=0
@SP
M=M+1
@R15
MD=M-1
@push.nVars.Class2.set
D;JGT
(stop.push.nVars.Class2.set)
//push argument 0 line 26
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
//pop static 0 line 27
@SP
AM=M-1
D=M
@Class2.0
M=D
//push argument 1 line 28
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
//pop static 1 line 29
@SP
AM=M-1
D=M
@Class2.1
M=D
//push constant 0 line 30
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//return line 31
@LCL
D=M
@R13
M=D
@5
D=D-A
A=D
D=M
@retAddr31
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@retAddr31
A=M
0;JMP
//function Class2.get 0 line 32
(Class2.get)
@0
D=A
@R15
M=D
@stop.push.nVars.Class2.get
D;JEQ
(push.nVars.Class2.get)
@SP
A=M
M=0
@SP
M=M+1
@R15
MD=M-1
@push.nVars.Class2.get
D;JGT
(stop.push.nVars.Class2.get)
//push static 0 line 33
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
//push static 1 line 34
@Class2.1
D=M
@SP
A=M
M=D
@SP
M=M+1
//sub line 35
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
AM=M+1
//return line 36
@LCL
D=M
@R13
M=D
@5
D=D-A
A=D
D=M
@retAddr36
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@retAddr36
A=M
0;JMP
//Endless Loop
(END)
@END
0;JMP
