# EasyCTF_2018: Fanfic Studio

**Category:** Binary Exploitation
**Points:** 350
**Description:**

>Go to `/problems/fanfic` to check out my cool fanfic writing tool. I expect you to send me some steamy fanfics of michael.

## Write-up
We are given two relevant files, [fanfic](fanfic) and [fanfic.c](fanfic.c). This is a relatively easy challenge where the goal is just to exploit the `chapter` structs. Firstly, the exploitable regions include the following,

    struct chapter {
        struct chapter *prev_chapter;
        struct chapter *next_chapter;
        char title[50];
        char content[256];
        void (* print_ch)(int, struct chapter *);
    };

and, 

    while (curr_ch != NULL) {
        curr_ch->print_ch(i, curr_ch);
        curr_ch = curr_ch->next_chapter;
        i++;
    }

In a nutshell, to crack the puzzle, two functions need to be called, `validate()` and `give_flag()`. We can get the addresses of these functions simply through radare2.

    [0x08048620]> afl
    [...]
    0x080487b4    3 22           sym.validate
    0x080487ca    1 37           sym.be_nice
    0x080487ef    9 147          sym.give_flag
    0x08048882   36 1423         main
    [...]

So now that we have our addresses, let's look at `validate()`. From an initial overview, it seems we just need to overwrite the `ans` variable to ensure when XORed with `0xDEADBEEF` gives `0xDEADBEAF`.

    int success = 0xFFFF;
    void validate(int ans) {
        if ((ans ^ 0xDEADBEEF) == 0xDEADBEAF) {
            success = 0xC001B4B3;
        }
    }

Reversing the equation, we get, 

    >>> 0xDEADBEAF ^ 0xDEADBEEF
    64

and since the code responsible for calling the function throws in the page number as the argument,

    i = 1;
    curr_ch = fanfic->first_chapter;
    while (curr_ch != NULL) {
        curr_ch->print_ch(i, curr_ch);
        curr_ch = curr_ch->next_chapter;
        i++;
    }

We just simply need to make this the 64th page. With `validate()` successfully called on the 64th page, we can then call `give_flag()` on the 65th page. Now, just simply pipe the [script](solve.py) to our exploitable fan fiction program!

    user55221@shell:~$ cd /problems/fanfic
    user55221@shell:/problems/fanfic$ ~/solve.py | /problems/fanfic/fanfic
    Please enter the title of your brand new fanfic: You have started writing the fanfic 'A'. Please select an option to get started!
    1. Edit chapter
    2. Delete chapter
    3. Publish fanfic
    > Enter chapter number to edit: Adding new chapter
    Enter chapter title: Enter chapter contents: 1. Edit chapter
    2. Delete chapter
    3. Publish fanfic
    [...]
    > Enter chapter number to edit: Adding new chapter
    Enter chapter title: Enter chapter contents: 1. Edit chapter
    2. Delete chapter
    3. Publish fanfic
    > Enter chapter number to edit: Editing chapter
    Enter new chapter text: 
    1. Edit chapter
    2. Delete chapter
    3. Publish fanfic
    > Enter chapter number to edit: Editing chapter
    Enter new chapter text: 
    1. Edit chapter
    2. Delete chapter
    3. Publish fanfic
    > Fanfic published! Here it is:
    ===============
    A
    ===============

    ---------------
    Chapter 1: A
    ---------------
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

    [...]
    ---------------
    Chapter 62: A
    ---------------
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

    ---------------
    Chapter 63: A
    ---------------
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    easyctf{h34p_expl01ts_ru1n1ng_my_f4nf1cs}

Therefore, the flag is `easyctf{h34p_expl01ts_ru1n1ng_my_f4nf1cs}`.
