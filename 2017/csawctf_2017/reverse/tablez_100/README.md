# CSAWCTF_2017: tablEZ

**Category:** Reverse
**Points:** 100
**Description:**

>Bobby was talking about tables a bunch, so I made some table stuff. I think this is what he was talking about...

## Write-up
This one was slightly tricky, we get started with the `main` fuction. Our pseudocode decompiler spits out the following for `main`,

    int main() {
        puts("Please enter the flag:");
        fgets(&var_90, 0x80, *__TMC_END__);
        *(int8_t *)(rbp + (strlen(&var_90) - 0x1) + 0xffffffffffffff70) = 0x0;
        var_C8 = strlen(&var_90);
        for (var_D0 = 0x0; var_D0 < var_C8; var_D0 = var_D0 + 0x1) {
                *(int8_t *)(var_D0 + &var_90) = get_tbl_entry(sign_extend_64(*(int8_t *)(var_D0 + &var_90) & 0xff));
        }
        if (var_C8 != 0x25) {
                puts("WRONG");
                rax = 0x1;
        }
        else {
                var_C0 = 0xb1e711f59d73b327;
                if (strncmp(&var_90, &var_C0, 0x26) == 0x0) {
                        puts("CORRECT <3");
                        rax = 0x0;
                }
                else {
                        puts("WRONG");
                        rax = 0x1;
                }
        }
        rsi = *0x28 ^ *0x28;
        if (rsi != 0x0) {
                rax = __stack_chk_fail();
        }
        return rax;
    }

Looks like the flag has something to do with having the processed string equals to `0xb1e711f59d73b327` but that doesn't make sense, considering we need a length of `37`! This is a lesson on the reliability of pseudocode decompilers. Going to assembly view, we get the following string.

    00000000000008ba         movabs     rax, 0xb1e711f59d73b327
    00000000000008c4         movabs     rdx, 0x30f4f9f9b399beb3
    00000000000008ce         mov        qword [rbp+var_C0], rax
    00000000000008d5         mov        qword [rbp+var_B8], rdx
    00000000000008dc         movabs     rax, 0xb19965237399711b
    00000000000008e6         movabs     rdx, 0xf9279923be111165
    00000000000008f0         mov        qword [rbp+var_B0], rax
    00000000000008f7         mov        qword [rbp+var_A8], rdx
    00000000000008fe         mov        dword [rbp+var_A0], 0x65059923
    0000000000000908         mov        word [rbp+var_9C], 0xce

This computes to `b1e711f59d73b32730f4f9f9b399beb3b19965237399711bf9279923be11116565059923ce`. How will we get the flag though? Well, this is actually computed through the `get_tbl_entry` fuction. Essentially, in steps of two, search through the `trans_tbl` table for the corresponding character and return the character above it. The trick is that because it checks from the base address while returning the address offsetted by 1, you pick the character above.

    b1 b
    e7 4
    11 t
    f5 {
    9d g
    73 a
    b3 l
    27 f

    30 u
    f4 k
    f9 0
    f9 0
    b3 l
    99 _
    be e
    b3 l

    b1 b
    99 _
    65 3
    23 r
    73 a
    99 _
    71 s
    1b p

    f9 0
    27 f
    99 _
    23 r
    be e
    11 t
    11 t
    65 3

    65 3
    05 m
    99 _
    23 r

    ce }

Therefore, the flag is `flag{t4ble_l00kups_ar3_b3tter_f0r_m3}`.
