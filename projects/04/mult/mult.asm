// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

    @R0
    D=M // set D to RAM[0] value
    @n
    M=D // n = R0
    @R1
    D=M // set D to RAM[1] value
    @m
    M=D // m = R1
    @i
    M=1 // i = 1
    @R2
    M=0 // set RAM[2] to 0
    @sum
    M=0 // sum = 0


    (LOOP)
    @i
    D=M // D = i
    @m
    D=D-M // D = i - RAM[1]
    @STOP
    D;JGT // if i - RAM[1] > 0 goto STOP

    @n
    D=M // D = n
    @sum
    M=M+D // sum = sum + D
    @i
    M=M+1 // i = i + 1
    @LOOP
    0;JMP

    (STOP)
    @sum
    D=M
    @R2
    M=D // RAM[2] = sum

    (END)
    @END
    0;JMP

