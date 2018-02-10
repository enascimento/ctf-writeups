# PACTF_2017: ETA

**Category:**
**Points:** 60
**Description:**

>If this script were to finish, what would it output? [MacOS](mac.out) [Linux](linux.out)

**Hint:**

>Try doing a bit of dynamic binary analysis. Read the registers!

## Write-up
This challenge is much easier with a proper x64-86 decompiler like IDA or Hopper. The function we are looking at here, is the `get_primes()` function.

    int _Z10get_primesm(long arg0) {
        var_38 = arg0;
        var_40 = rsi;
        rdi = var_38;
        rax = std::vector<unsigned long, std::allocator<unsigned long> >::vector();
        var_20 = operator new[]((var_40 >> 0x3) + 0x1);
        rax = memset(var_20, 0xff, (var_40 >> 0x3) + 0x1);
        for (var_28 = 0x2; var_28 <= var_40; var_28 = var_28 + 0x1) {
                if ((SAR(sign_extend_64(*(int8_t *)(var_20 + (var_28 >> 0x3)) & 0xff), (var_28 & 0x7)) & 0x1) != 0x0) {
                        rsi = var_28;
                        rax = std::vector<unsigned long, std::allocator<unsigned long> >::push_back(var_38);
                        for (var_18 = var_28 + var_28; var_18 <= var_40; var_18 = var_18 + var_28) {
                                *(int8_t *)(var_20 + (var_18 >> 0x3)) = *(int8_t *)((var_18 >> 0x3) + var_20) & 0xff & !(0x1 << (var_18 & 0x7));
                        }
                }
        }
        if (var_20 != 0x0) {
                rax = operator delete[](var_20);
        }
        rax = var_38;
        rbx = stack[2046];
        rsp = rsp + 0x48;
        rbp = stack[2047];
        return rax;
    }

We need to look closer at the part of the pseudocode that will give us the solution.

    for (var_28 = 0x2; var_28 <= var_40; var_28 = var_28 + 0x1) {

The base idea of this part of the code, refers to how it's actually looking for THE largest prime number that's smaller than `var_40`, which is `2147483644`. With some clever searching, the largest prime number smaller than `2147483644` is, `2147483629`.

Therefore, the flag is `2147483629`.