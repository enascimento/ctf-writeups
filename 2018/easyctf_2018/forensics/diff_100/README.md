# EasyCTF_2018: Diff

**Category:** Forensics
**Points:** 100
**Description:**

>Sometimes, the differences matter. Especially between the files in this [archive](file.tar).
Hint: This is a TAR archive file. You can extract the files inside this tar by navigating to the directory where you downloaded it and running tar xf file.tar! If you don't have tar on your personal computer, you could try doing it from the Shell server. Once you extract the files, try comparing the hex encodings of the files against the first file.

## Write-up
This challenge was really simple and simply required proper DIFFing of the files. To start off, simply `xxd` all the files to their hex encoded counterpart,

    # xxd file > file.hex
    # xxd file2 > file2.hex
    # xxd file3 > file3.hex
    # xxd file4 > file4.hex

Then simply compare!

    # diff -a file.hex file2.hex
    1c1
    < 00000000: 7f45 4c46 0201 0100 0000 0000 0000 0000  .ELF............
    ---
    > 00000000: 7f45 4c46 0201 0100 0065 0000 0000 0000  .ELF.....e......
    8c8
    < 00000070: 0800 0000 0000 0000 0300 0000 0400 0000  ................
    ---
    > 00000070: 0800 0000 0000 0000 0361 0000 0400 0000  .........a......
    15c15
    < 000000e0: 0000 2000 0000 0000 0100 0000 0600 0000  .. .............
    ---
    > 000000e0: 0000 2000 0000 0000 0100 7300 0600 0000  .. .......s.....
    18,19c18,19
    < 00000110: 9802 0000 0000 0000 0000 2000 0000 0000  .......... .....
    < 00000120: 0200 0000 0600 0000 f80d 0000 0000 0000  ................
    ---
    > 00000110: 9802 0000 7963 7400 0000 2000 0000 0000  ....yct... .....
    > 00000120: 0200 0000 0600 6600 f80d 0000 0000 0000  ......f.........
    25c25
    < 00000180: 4400 0000 0000 0000 0400 0000 0000 0000  D...............
    ---
    > 00000180: 4400 0000 0000 007b 0400 0000 0000 0000  D......{........
    31c31
    < 000001e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    ---
    > 000001e0: 0000 0000 0000 0064 0000 0000 0000 0000  .......d........
    59c59
    < 000003a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    ---
    > 000003a0: 0000 0000 0000 0069 0000 0000 0000 0000  .......i........
    558a559
    > 000022e0: 0a 

From the first few lines, we can something really interesting already,

    1c1
    < 00000000: 7f45 4c46 0201 0100 0000 0000 0000 0000  .ELF............
    ---
    > 00000000: 7f45 4c46 0201 0100 0065 0000 0000 0000  .ELF.....e......
    8c8
    < 00000070: 0800 0000 0000 0000 0300 0000 0400 0000  ................
    ---
    > 00000070: 0800 0000 0000 0000 0361 0000 0400 0000  .........a......
    15c15
    < 000000e0: 0000 2000 0000 0000 0100 0000 0600 0000  .. .............
    ---
    > 000000e0: 0000 2000 0000 0000 0100 7300 0600 0000  .. .......s.....
    18,19c18,19
    < 00000110: 9802 0000 0000 0000 0000 2000 0000 0000  .......... .....
    < 00000120: 0200 0000 0600 0000 f80d 0000 0000 0000  ................
    ---
    > 00000110: 9802 0000 7963 7400 0000 2000 0000 0000  ....yct... .....
    > 00000120: 0200 0000 0600 6600 f80d 0000 0000 0000  ......f.........

Comparing the differences in each line, you get the letters `easyctf`. Where do we go from this? Well, after comparing `file.hex` with `file2.hex`, `file3.hex` and `file4.hex`, you get the flag!

    # diff -a file.hex file2.hex
    1c1
    < 00000000: 7f45 4c46 0201 0100 0000 0000 0000 0000  .ELF............
    ---
    > 00000000: 7f45 4c46 0201 0100 0065 0000 0000 0000  .ELF.....e......
    8c8
    < 00000070: 0800 0000 0000 0000 0300 0000 0400 0000  ................
    ---
    > 00000070: 0800 0000 0000 0000 0361 0000 0400 0000  .........a......
    15c15
    < 000000e0: 0000 2000 0000 0000 0100 0000 0600 0000  .. .............
    ---
    > 000000e0: 0000 2000 0000 0000 0100 7300 0600 0000  .. .......s.....
    18,19c18,19
    < 00000110: 9802 0000 0000 0000 0000 2000 0000 0000  .......... .....
    < 00000120: 0200 0000 0600 0000 f80d 0000 0000 0000  ................
    ---
    > 00000110: 9802 0000 7963 7400 0000 2000 0000 0000  ....yct... .....
    > 00000120: 0200 0000 0600 6600 f80d 0000 0000 0000  ......f.........
    25c25
    < 00000180: 4400 0000 0000 0000 0400 0000 0000 0000  D...............
    ---
    > 00000180: 4400 0000 0000 007b 0400 0000 0000 0000  D......{........
    31c31
    < 000001e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    ---
    > 000001e0: 0000 0000 0000 0064 0000 0000 0000 0000  .......d........
    59c59
    < 000003a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    ---
    > 000003a0: 0000 0000 0000 0069 0000 0000 0000 0000  .......i........
    558a559
    > 000022e0: 0a 

    FLAG: easyctf{di

    # diff -a file.hex file3.hex
    12c12
    < 000000b0: 0100 0000 0500 0000 0000 0000 0000 0000  ................
    ---
    > 000000b0: 0100 6600 0500 0000 0000 0000 0000 0000  ..f.............
    17c17
    < 00000100: e00d 6000 0000 0000 7c02 0000 0000 0000  ..`.....|.......
    ---
    > 00000100: e00d 6000 6600 0000 7c02 0000 0000 0000  ..`.f...|.......
    32c32
    < 000001f0: 0000 0000 0000 0000 1000 0000 0000 0000  ................
    ---
    > 000001f0: 0000 0000 0069 0000 1000 0000 0000 0000  .....i..........
    50c50
    < 00000310: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    ---
    > 00000310: 0000 0000 006e 6900 0000 0000 0000 0000  .....ni.........
    61c61
    < 000003c0: 0000 0000 0000 0000 8b00 0000 1200 0000  ................
    ---
    > 000003c0: 0000 0000 0000 746c 8b00 0000 1200 0000  ......tl........
    273c273
    < 00001100: 5f72 002e 7265 6c61 2e64 796e 002e 7265  _r..rela.dyn..re
    ---
    > 00001100: 5f72 002e 7265 795f 2e64 796e 002e 7265  _r..rey_.dyn..re
    283c283
    < 000011a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    ---
    > 000011a0: 0000 0000 0000 616e 5f00 0000 0000 0000  ......an_.......
    558a559
    > 000022e0: 0a

    FLAG: easyctf{di + ffinitly_an_

    # diff -a file.hex file4.hex
    79c79
    < 000004e0: 0200 0200 0200 0200 0200 0000 0000 0000  ................
    ---
    > 000004e0: 657a 0200 5f70 726f 626c 656d 217d 0000  ez.._problem!}..
    558a559
    > 000022e0: 0a    

    FLAG: easyctf{diffinitly_an_ + ez_problem!}

Therefore, the flag is `easyctf{diffinitly_an_ez_problem!}`