#! /usr/bin/env python
##
from socket import socket
# from asm import Asm
from subprocess import CalledProcessError, check_output

import sys
import time
import re
import atexit

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

def remove_unnecessary_data(data):
    lines = []
    for code in re.findall('(?:\n)[a-z]+\s.*', data):
        lines.append(code)
    return ''.join(lines).strip()

def get_question(data):
    return re.findall('(?:\n)([a-z]{3})(?:\:)', data)[0]

def invert_register(register):
    register = [ch for ch in register]
    if register[0] == "r":
        register[0] = "e"
    register = ''.join(register)
    return register

def parse_registers(debug):
    registers = {}
    for i in re.findall('([a-z0-9]+\s=\s0x[a-z0-9]+)', debug):
        try:
            args = i.split(' ')
            register = args[0]
            value = int(args[2], 16)
            registers[register] = value

            value = 0xFFFFFFFF & value
            registers[invert_register(register)] = value
        except IndexError:
            pass
    return registers

def reset_sane():
    print(check_output(['stty', 'sane']))

atexit.register(reset_sane)

while True:
    s = socket()
    s.connect(('play.spgame.site', 1351))

    while True:
        data = ""
        while ':' not in data:
            data += s.recv(4096)

        if data != '':
            data = data.strip()
            if '/200' in data:
                print(data.strip())
                stripped_asm = remove_unnecessary_data(data)

                code = asm_header + stripped_asm + asm_footer
                with open('code.asm', 'w') as file:
                    for line in code.split('\n'):
                        file.write(line + "\n")

                compiler_debug = ""
                try:
                    check_output(['nasm', '-f', 'elf64', 'code.asm'])
                    check_output(['ld', 'code.o'])
                    compiler_debug = check_output(['lldb', '-o', 'b exit', '-o', 'run', '-o', 'register read', '-o', 'script import os; os._exit(1)', 'a.out'])
                except CalledProcessError as err:
                    compiler_debug = err.output
                    pass

                question = get_question(data)
                registers = parse_registers(compiler_debug)

                response = str(registers[question])
                print("%s = %s" % (question, response))
                time.sleep(0.01)
                s.send(response + "\n")
                continue
            elif 'Wrong' in data:
                print(data)
                sys.exit(0)
            else:
                print(data)