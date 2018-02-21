# EasyCTF_2018: Linux

**Category:** Intro
**Points:** 10
**Description:**

>Log into the shell server! You can do this in your browser by clicking on the Shell server link in the dropdown in the top right corner, or using an SSH client by following the directions on that page.
Once you've logged in, you'll be in your home directory. We've hidden something there! Try to find it. :)

## Write-up
Another simple challenge, involving SSH.

    root@ctf:~# ssh user55221@s.easyctf.com
    The authenticity of host 's.easyctf.com (165.227.212.254)' can't be established.
    ECDSA key fingerprint is SHA256:CNCQb5MB2MSas+mn3naxQUK0U6diDChNC5Des+902ME.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added 's.easyctf.com,165.227.212.254' (ECDSA) to the list of known hosts.
    user55221@s.easyctf.com's password: 
      ______                 _____ _______ ______ 
     |  ____|               / ____|__   __|  ____|
     | |__   __ _ ___ _   _| |       | |  | |__   
     |  __| / _` / __| | | | |       | |  |  __|  
     | |___| (_| \__ \ |_| | |____   | |  | |     
     |______\__,_|___/\__, |\_____|  |_|  |_|     
                       __/ |                      
                      |___/                       

        Welcome to EasyCTF IV's Shell server!

    == Questions? Bugs? Let us know on Discord ==
    ==       https://discord.gg/UxCJxf4        ==

    Rules:
      1. If you aren't sure if you should be doing
         something, ask an organizer or don't do
         it.
      2. Be nice to people.

    If there's any software that you'd like to have
    installed, let one of the organizers know on
    Discord!

    Last login: Sun Feb 11 03:03:52 2018 from 173.245.48.85

Doing a bit of sleuthing, we find a hidden file `.flag`.

    user55221@shell:~$ ls -lah
    total 28K
    drwx------  3 user55221 ctfuser 4.0K Feb 11 03:04 .
    drwxr-xr-x 61 root      root    4.0K Feb 11 03:05 ..
    -rw-r--r--  1 user55221 ctfuser  220 Aug 31  2015 .bash_logout
    -rw-r--r--  1 user55221 ctfuser 3.7K Aug 31  2015 .bashrc
    drwx------  2 user55221 ctfuser 4.0K Feb 11 03:04 .cache
    -rw-r--r--  1 user55221 ctfuser    0 Feb  7 13:52 .cloud-locale-test.skip
    -rw-r--r--  1 user55221 ctfuser   41 Feb  7 13:41 .flag
    -rw-r--r--  1 user55221 ctfuser  655 May 16  2018 .profile

Next, just `cat` it!

    user55221@shell:~$ cat .flag
    easyctf{i_know_how_2_find_hidden_files!}

Therefore, the flag is `easyctf{i_know_how_2_find_hidden_files!}`.
