# AngstromCTF_2018: Rev2

**Category:** Reverse
**Points:** 80
**Description:**

>It's time for Rev2! This one is pretty similar to the first: once you get the inputs right to the program, you will get the flag. You don't need the shell server for this one, but the binary can be found at `/problems/rev2/` if you would like to run it there.

## Write-up
This challenge involves reading some assembly,

    │           0x0804853b      e890feffff     call sym.imp.__isoc99_scanf
    │           0x08048540      83c410         add esp, 0x10
    │           0x08048543      8b45e4         mov eax, dword [local_1ch]
    │           0x08048546      3dd7110000     cmp eax, 0x11d7

This part above looks for a number equals to `0x11d7` or `4567`.

    │      │    0x0804858b      e840feffff     call sym.imp.__isoc99_scanf
    │      │    0x08048590      83c410         add esp, 0x10
    │      │    0x08048593      8b45e8         mov eax, dword [local_18h]
    │      │    0x08048596      83f863         cmp eax, 0x63               ; 'c' ; 99
    │      │┌─< 0x08048599      7f22           jg 0x80485bd
    │      ││   0x0804859b      8b45e8         mov eax, dword [local_18h]
    │      ││   0x0804859e      83f809         cmp eax, 9                  ; 9
    │     ┌───< 0x080485a1      7e1a           jle 0x80485bd
    │     │││   0x080485a3      8b45ec         mov eax, dword [local_14h]
    │     │││   0x080485a6      83f863         cmp eax, 0x63               ; 'c' ; 99
    │    ┌────< 0x080485a9      7f12           jg 0x80485bd
    │    ││││   0x080485ab      8b45ec         mov eax, dword [local_14h]
    │    ││││   0x080485ae      83f809         cmp eax, 9                  ; 9
    │   ┌─────< 0x080485b1      7e0a           jle 0x80485bd
    │   │││││   0x080485b3      8b55e8         mov edx, dword [local_18h]
    │   │││││   0x080485b6      8b45ec         mov eax, dword [local_14h]
    │   │││││   0x080485b9      39c2           cmp edx, eax

The next part aboves checks that both numbers on part 2, is smaller than or equals to 99 but bigger than 9.

    │      ││   0x080485da      0fafc2         imul eax, edx
    │      ││   0x080485dd      8945f0         mov dword [local_10h], eax
    │      ││   0x080485e0      817df0670d00.  cmp dword [local_10h], 0xd67 ; [0xd67:4]=-1 ; 3431

This part checks that our lovely second input has to multiple together to form `0xd67` or `3431`. This factors out nicely to `47` and `73`. Therefore, by now running it with all of our gathered inputs, we get

    $ ./rev2_32 
    Welcome to Rev2! You'll probably want to use a dissassembler or gdb.
    Level 1: What number am I thinking of: 4567
    Level 2: Which two two-digit numbers will solve this level. Enter the two numbers separated by a single space (num1 should be the lesser of the two): 47 73
    Congrats, you passed Rev2! The flag is: actf{4567_47_73}

Therefore, the flag is `actf{4567_47_73}`.
