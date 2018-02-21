# EasyCTF_2018: Liar

**Category:** Reverse
**Points:** 70
**Description:**

>Sometimes, developers put their source into their code with -g. Sometimes, they put another source into their code with -g.
[executable](getflag)
[source](getflag.c)

## Write-up
This challenge relied on the disasembly of the executable to find out that `1337` was indeed not the value to use. In fact, upon disassembly of the code, you find a really interesting number.

    │           0x5555555548f0      8b45ec         mov eax, dword [input]
    │           0x5555555548f3      3529eb5800     xor eax, 0x58eb29

`0x58eb29` is also `5827369`. However, using it doesn't give us our flag either,

    # ./getflag 
    5827369

Now what? Well, if we look closely, the input is being used as a variable to some form of XOR operations, 

    │           0x5555555548f0      8b45ec         mov eax, dword [input]
    │           0x5555555548f3      3529eb5800     xor eax, 0x58eb29
    │           0x5555555548f8      8945f4         mov dword [local_ch], eax
    │           0x5555555548fb      c745f0000000.  mov dword [loops], 0
    │       ┌─< 0x555555554902      eb41           jmp 0x555555554945
    │      ┌──> 0x555555554904      8b45f0         mov eax, dword [loops]
    │      ⁝│   0x555555554907      4898           cdqe
    │      ⁝│   0x555555554909      488d14c50000.  lea rdx, [rax*8]
    │      ⁝│   0x555555554911      488d05480720.  lea rax, obj.f          ; 0x555555755060 ; "e"
    │      ⁝│   0x555555554918      488b0402       mov rax, qword [rdx + rax]
    │      ⁝│   0x55555555491c      89c6           mov esi, eax
    │      ⁝│   0x55555555491e      8b45f0         mov eax, dword [loops]
    │      ⁝│   0x555555554921      89c1           mov ecx, eax
    │      ⁝│   0x555555554923      8b45f4         mov eax, dword [local_ch]
    │      ⁝│   0x555555554926      89c2           mov edx, eax
    │      ⁝│   0x555555554928      89c8           mov eax, ecx
    │      ⁝│   0x55555555492a      0fafc2         imul eax, edx
    │      ⁝│   0x55555555492d      89f1           mov ecx, esi
    │      ⁝│   0x55555555492f      31c1           xor ecx, eax
    │      ⁝│   0x555555554931      8b45f0         mov eax, dword [loops]
    │      ⁝│   0x555555554934      4863d0         movsxd rdx, eax
    │      ⁝│   0x555555554937      488d05620820.  lea rax, obj.g          ; 0x5555557551a0 ; "e\x0f\xafW\xdbZ:\x95\x03\xfa5\xa2\xd4Q\xab/\x93\xe0;:\xe7z\xf3\xa1/\x8c}\u0294q\xee\x07\xa7\x06h\x91E"
    │      ⁝│   0x55555555493e      880c02         mov byte [rdx + rax], cl
    │      ⁝│   0x555555554941      8345f001       add dword [loops], 1
    │      :│      ; JMP XREF from 0x555555554902 (main)
    │      ⁝└─> 0x555555554945      837df024       cmp dword [loops], 0x24 ; [0x24:4]=-1 ; '$' ; 36
    │      └──< 0x555555554949      7eb9           jle 0x555555554904

Through a bit of trial and error, we get the proper key, which was `5827374`.

    # ./getflag 
    5827374
    the flag is easyctf{still_wasn't_too_bad,_right?}

Therefore, the flag is `easyctf{still_wasn't_too_bad,_right?}`.
