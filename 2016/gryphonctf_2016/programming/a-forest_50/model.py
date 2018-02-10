from pwn import *
from keystone import *
from unicorn import *
from unicorn.x86_const import *
import ctypes

#context.log_level = "debug"

registers = {'eax': UC_X86_REG_EAX, 'rax': UC_X86_REG_RAX,
             'ebx': UC_X86_REG_EBX, 'rbx': UC_X86_REG_RBX,
             'ecx': UC_X86_REG_ECX, 'rcx': UC_X86_REG_RCX,
             'edx': UC_X86_REG_EDX, 'rdx': UC_X86_REG_RDX,
             'esi': UC_X86_REG_ESI, 'rsi': UC_X86_REG_RSI,
             'edi': UC_X86_REG_EDI, 'rdi': UC_X86_REG_RDI
             }

def emulate(bytecode, chosen_register):
    code = "".join(map(chr, bytecode))
    mu = Uc(UC_ARCH_X86, UC_MODE_64)
    ADDRESS = 0x1000000
    STACK_ADDRESS = 0x2000000
    STACK_END_ADDRESS = STACK_ADDRESS + (1 * 512 * 1024)
    mu.mem_map(ADDRESS, 1 * 1024 * 1024)
    mu.mem_map(STACK_ADDRESS, 1 * 512 * 1024)
    mu.reg_write(UC_X86_REG_RSP, STACK_END_ADDRESS)
    mu.mem_write(ADDRESS, code)
    mu.emu_start(ADDRESS, ADDRESS + len(code))
    reg = mu.reg_read(registers[chosen_register])
    return reg

def main():
    p = remote("play.spgame.site", 1351)
    p.recvline_contains('Please present your answers as unsigned 64 bit decimal integers')
    ks = Ks(KS_ARCH_X86, KS_MODE_64)
    for i in range(1, 201):
        p.recvline()
        data = p.recvuntil(": ").split('\n')
        instructions, register = data[:-1], data[-1].split(":")[0]
        bytecode, count = ks.asm("\n".join(instructions))
        result = emulate(bytecode, register)
        result = ctypes.c_uint64(result).value
        p.sendline(str(result))
        log.info("%d) No. of Instructions: %d | %s: %d" % (i, len(instructions),
                                                           register, result))

    flag = p.recvall()
    log.success(flag)

if __name__ == "__main__":
    main()