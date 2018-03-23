# AngstromCTF_2018: Source Me 1

**Category:** Web
**Points:** 20
**Description:**

>There is only one goal: [Log in](http://web.angstromctf.com:6999/).

## Write-up
The page source tells us the password.

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Source Me 1</title>
    </head>
    <body>
    <h2>Welcome to the admin portal!</h2>
    Currently, only the user who can login is 'admin'.
    <br>
    <!-- Shh, don't tell anyone. The admin password is f7s0jkl -->
    <form action="./login.php" method="get">
    Username:<input type="text" name = "user"><br>
    Password:<input type="text" name = "pass"><br>
    <input type="submit" value="Submit">
    </form>
    </body>
    </html>

Attempting to log in with the username `admin` and password `f7s0jkl`, we get the flag.

    Welcome, admin. Here is your flag: actf{source_aint_secure}

Therefore, the flag is `actf{source_aint_secure}`.
