# GryphonCTF_2016: The Forest

**Category:** Programming
**Points:** 50
**Description:**

>It is time to test your 1337 skills of doing assembly in your head.
You get ten seconds to evaluate the given x86-64 code listing and give us the value of the register that has been randomly chosen from those modified.
Assembly! Again, and again, and again, and again, and again...

## Write-up
As the challenge description goes, we need to evaluate the given x84-64 assembly code and return the value of the register randomly selected. For 200 times. If you tried doing this in your head, I applaud you, simply because,

    ==== 200/200 ====
    xor rdx, rsi
    add edx, edx
    xor eax, 0xb8f4e2
    mov rbx, 0x18781004fdca0ede
    mov ebx, edx
    mov rcx, 0x47a64db738b73d65
    lea esi, [rbx+rax]
    mov edx, esi
    and rbx, rbx
    xor rsi, rdx
    lea rsi, [rbx+rax]
    add edi, 0x490e8d
    sub edi, 0xd09331
    and ecx, 0xd3d93b
    and ecx, 0x7b3147
    push rdx
    xor eax, 0x7b8d46
    add edx, 0x2112c5
    mov eax, esi
    xor edx, edx
    mov esi, 0xe28e5d23fea53496
    lea ecx, [eax+0x23c005]
    add rcx, 0x59accd
    and rbx, rdi
    add rcx, rcx
    mov rsi, rcx
    xor ecx, edx
    push rdx
    sub ecx, 0xccd275
    mov edi, 0xb83649e57125aff
    pop rax
    mov edi, ebx
    and rsi, rdi
    and ebx, esi
    push rcx
    lea rax, [edx+eax]
    and ebx, 0xdf99a5
    mov rcx, rcx
    add eax, 0x3a227
    xor ebx, 0x539bd9
    pop rdi
    lea rcx, [edx+0xfff539]
    lea ecx, [rdx+0x29fa14]
    pop rbx
    inc rsi
    lea edx, [edi+0x690cd7]
    lea rsi, [rsi+0xe89a6b]
    mov rbx, rax
    mov edi, eax
    push rcx
    push rsi
    lea esi, [edx+edx]
    sub esi, 0xeb3ff9
    pop rax
    add rdx, rax
    add rbx, 0xcabc14
    add edi, ebx
    add rsi, 0x5e5c5d
    inc rsi
    sub rdx, 0xb333f8
    lea rax, [rsi+rbx]
    lea rax, [ecx+ebx]
    push rcx
    xor eax, 0xd860e1
    xor ecx, 0xeca0a8
    add rcx, 0x53772d
    lea rdx, [rcx+rsi]
    lea rsi, [rdi+rdx]
    sub ecx, esi
    lea rsi, [edi+ecx]
    and rsi, rdi
    mov esi, eax
    and rcx, 0xe52d8
    add rax, rdx
    lea ecx, [ecx+eax]
    xor rcx, 0xad1fc6
    push rdx
    lea rdi, [edx+ebx]
    and edx, edx
    add esi, edi
    and edx, 0xfaa4c7
    lea rsi, [rdi+0xa38903]
    inc rdi
    and rcx, 0x5cce3
    sub edx, ebx
    mov ebx, edi
    lea rsi, [rsi+rbx]
    mov ecx, edx
    inc rdx
    lea esi, [rbx+0xdf259f]
    add rax, rdx
    lea rsi, [ebx+0x1a6f]
    lea rsi, [rdi+0x7b4c0b]
    and rax, rsi
    inc rdi
    lea rbx, [rdx+0x1ae3f4]
    lea rsi, [rdx+rdi]
    sub esi, 0x56dbb8
    add rsi, 0x9d35e5
    add eax, edx
    add edi, esi
    pop rbx
    add ebx, 0xf18bf5
    sub edi, 0x823ae2
    mov edx, ebx
    add edi, ecx
    xor rsi, 0x3707c7
    inc esi
    and eax, ecx
    sub rbx, 0xfc8030
    xor esi, eax
    and rbx, 0xfa3cf4
    mov eax, ebx
    push rcx
    xor edx, 0x75c2c
    add rdx, rdi
    add edi, 0x8f1f83
    push rsi
    add rdi, rdx
    pop rcx
    add eax, ebx
    and rcx, rcx
    and esi, 0x9c3d6f
    and ecx, 0xaf5149
    lea rdx, [ebx+0xa8150c]
    xor edx, 0xba2a9d
    mov rbx, 0x9308aa2cd80fcd13
    inc ecx
    push rcx
    push rdx
    and eax, 0xd4ed
    lea ecx, [ebx+edx]
    sub edi, edi
    lea rdi, [rdx+0x719b4e]
    lea edi, [edi+edx]
    lea ebx, [rdi+rax]
    sub rdi, rcx
    mov rdi, rbx
    xor rdi, 0xdf8561
    and rbx, rdi
    add esi, ecx
    xor ecx, 0xd54069
    mov edx, 0x59560b73babacdab
    xor rdx, rdi
    sub edi, edx
    mov rsi, rbx
    xor edi, edi
    sub rbx, rdi
    and ebx, 0x87f93b
    pop rdi
    xor eax, 0x7ffef7
    xor esi, 0x84ffec
    pop rdx
    mov edx, edi
    add rsi, rdi
    inc rcx
    pop rcx
    add esi, 0x67ce21
    add rdx, 0xd999e
    and edi, 0xefb0ec
    xor esi, edx
    add eax, edi
    push rdi
    mov esi, ebx
    xor rdx, rax
    pop rbx
    push rdi
    xor rax, 0x55ead2
    inc rax
    xor esi, 0xcb46f
    push rdi
    push rax
    lea rbx, [rbx+0xc2917d]
    and rdi, 0x50f7c4
    push rdx
    add eax, 0xd14be4
    push rdi
    add eax, esi
    mov ecx, esi
    xor rax, rax
    mov esi, ebx
    pop rax
    and esi, 0x64983e
    lea edx, [rsi+rdi]
    xor rcx, 0x5ea9f4
    xor rax, 0x3a6f39
    mov edx, edx
    lea edx, [esi+0x537f04]
    sub rbx, rdx
    inc rbx
    inc rdi
    xor rbx, rsi
    inc rdx
    xor ecx, edx
    lea eax, [ecx+0x7a6a18]
    xor rsi, 0x7f2c11
    lea rax, [rsi+0xfa1c3a]
    xor ebx, 0x72141
    xor rbx, rdi
    and ebx, eax
    lea edi, [rcx+rbx]
    inc rax
    xor ebx, ecx
    xor rax, 0xc99bf8
    rdi:

was the length of the 200th iteration.

To solve this, you need to understand how to compile machine code, specifically, x86-64 code. You could try writing your own language interpreter for ASM, or you could just script `nasm` and `ld` into your code.

Firstly, make a template.

    asm_header = """global start
    section .data

    section .text

    start:
    """

    asm_footer = """
        je      exit
    exit:
        mov     eax, 01h        ; exit()
        xor     ebx, ebx        ; errno
        int     80h"""

Then, connect to the server and obtain JUST the ASM part. Contanectate the `asm_header`, the `asm_code` and the `asm_footer`, write it to a file, preferably with an extension `.asm` and call commands like

    $ nasm -f elf64 code.asm
    $ ld code.o

This compiles `code.asm` to `code.o` and then compiles `code.o` to `a.out`. Following that, you can now try running `lldb` as a debugger.

    $ lldb a.out

Setting a breakpoint at the exit function, allows you to view the register before it exits.

    (lldb) b exit
    Breakpoint 1: where = a.out`exit, address = 0x000000000040039e

Try running and you get,

    (lldb) run
    Process 12213 launched: '/root/forest/a.out' (x86_64)
    Process 12213 stopped
    * thread #1: tid = 12213, 0x000000000040039e a.out`exit, name = 'a.out', stop reason = breakpoint 1.1
        frame #0: 0x000000000040039e a.out`exit
    a.out`exit:
    -> 0x40039e:  movl   $0x1, %eax
       0x4003a3:  xorl   %ebx, %ebx
       0x4003a5:  int    $-0x80
       0x4003a7:  addb   %ch, (%rsi)

Now, dump the register by running, `register read`.

    (lldb) register read
    General Purpose Registers:
           rax = 0x0000000001f0438c
           rbx = 0x0000000000ef22b4
           rcx = 0x0000000000c632a6
           rdx = 0x0000000000940f2d
           rdi = 0x0000000000ef42b8
           rsi = 0x00000000003fbc39
           rbp = 0x0000000000000000
           rsp = 0x00007ffc5e9603b0
            r8 = 0x0000000000000000
            r9 = 0x0000000000000000
           r10 = 0x0000000000000000
           r11 = 0x0000000000000000
           r12 = 0x0000000000000000
           r13 = 0x0000000000000000
           r14 = 0x0000000000000000
           r15 = 0x0000000000000000
           rip = 0x000000000040039e  a.out`exit
        rflags = 0x0000000000000202
            cs = 0x0000000000000033
            fs = 0x0000000000000000
            gs = 0x0000000000000000
            ss = 0x000000000000002b
            ds = 0x0000000000000000
            es = 0x0000000000000000

See how it's all nicely laid out for us? We can shorten the lldb command to just simply

    $ lldb -o 'b exit' -o run -o 'register read' -o 'script import os; os._exit(1)' a.out
    Current executable set to 'a.out' (x86_64).
    Breakpoint 1: where = a.out`exit, address = 0x000000000040039e
    (lldb) Process 12586 launched: '/root/forest/a.out' (x86_64)
    General Purpose Registers:
           rax = 0x0000000001f0438c
           rbx = 0x0000000000ef22b4
           rcx = 0x0000000000c632a6
           rdx = 0x0000000000940f2d
           rdi = 0x0000000000ef42b8
           rsi = 0x00000000003fbc39
           rbp = 0x0000000000000000
           rsp = 0x00007ffe6a1829a0
            r8 = 0x0000000000000000
            r9 = 0x0000000000000000
           r10 = 0x0000000000000000
           r11 = 0x0000000000000000
           r12 = 0x0000000000000000
           r13 = 0x0000000000000000
           r14 = 0x0000000000000000
           r15 = 0x0000000000000000
           rip = 0x000000000040039e  a.out`exit
        rflags = 0x0000000000000202
            cs = 0x0000000000000033
            fs = 0x0000000000000000
            gs = 0x0000000000000000
            ss = 0x000000000000002b
            ds = 0x0000000000000000
            es = 0x0000000000000000

Now, we can all script it together in a python script. You can choose to run a regex through the output of `lldb` to get pairs of register and hex value. You realize that there is no `eax` and similar registers, because they are 32bit registers. You can generate their values by running `0xFFFFFFFF` AND operation before storing it in the 32 bit 'register'.

However, somewhere along the lines of 80+ tries, it stops working.

    ld: warning: cannot find entry symbol _start; defaulting to 0000000000400080
    Traceback (most recent call last):
      File "./script.py", line 87, in <module>
        question = get_question(data)
      File "./script.py", line 34, in get_question
        return re.findall('(?:\n)([a-z]{3})(?:\:)', data)[0]
    IndexError: list index out of range

This is caused by server-side sock buffer and thus you can solve it via,

    data = ""
    while ':' not in data:
        data += s.recv(4096)

to ensure that as long as the question is not asked, keep receiving data.

You can view the [full script I used here.](script.py)

Therefore, the flag is, `GCTF{cau53_b0y5_d0nt_cry}`.
