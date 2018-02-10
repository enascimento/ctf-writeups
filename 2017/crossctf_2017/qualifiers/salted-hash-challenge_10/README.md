# CrossCTF_2017: Salted Hash Challenge

**Category:** Web
**Points:** 10
**Description:**

>I've logged in with my admin credentials:
Admin username: john
Admin password: moreThan10CharPassword
I am supposed to get have admin privileges, but the webpage keeps telling me I am not admin. I must have configured something wrongly, can you help me? 
Please find the website hosted on 128.199.98.78:32769/index.php

## Write-up
A challenge on mysterious salts. For this challenge, we have no clue what the salt is so trying to bruteforce it is ridiculous. Let's try something new, also known as a Length Extension Attack on hashes.

We will be using [Hashpump](https://github.com/bwall/HashPump) to help us on this one, credits to (@kaikai) for solving this originally before I reworked my solution to actually work.

[Solution](solve.py)

    $ ./solve.py 
    <h1>Admin</h1>Here's your flag: CrossCTF{thIs_H@5h_iz_5Alty}

Therefore, the flag is `CrossCTF{thIs_H@5h_iz_5Alty}`.