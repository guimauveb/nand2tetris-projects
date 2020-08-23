// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(STATUS)
    @KBD
    D=M // check if keyboard > 0
    @BLACK
    D;JGT
    @KBD
    D=M // check if keyboard = 0
    @WHITE 
    D;JEQ

(BLACK)
    @SCREEN 
    D=A // D = SCREEN address  
    @addr
    M=D // addr = 16384
    @8191
    D=A // set D to 8191
    @n
    M=D // n = 8191
    @i
    M=0 // i = 0
    (LOOPBLACK)
        @i
        D=M // D = i
        @n
        D=D-M // check if i - 8191 > 0
        @STATUS
        D;JGT
        @addr
        A=M // [addr] = 16384
        M=-1 // RAM[addr] = 1111111111111111
        @i
        M=M+1   // i = i + 1
        @addr
        M=M+1 // addr = addr + 1
        @LOOPBLACK
        0;JMP // goto LOOPBLACK

(WHITE)
    @SCREEN 
    D=A // D = SCREEN address  
    @addr
    M=D // addr = 16384
    @8191
    D=A // set D to 8191
    @n
    M=D // n = 8191
    @i
    M=0 // i = 0
    (LOOPWHITE)
        @i
        D=M // D = i
        @n
        D=D-M // check if i - 8191 > 0
        @STATUS
        D;JGT
        @addr
        A=M // [addr] = 16384
        M=0 // RAM[addr] = 0000000000000000
        @i
        M=M+1   // i = i + 1
        @addr
        M=M+1 // addr = addr + 1
        @LOOPWHITE
        0;JMP // goto LOOPWHITE


