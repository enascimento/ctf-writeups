# GryphonCTF_2016: HARAMBE

**Category:** Web
**Points:** 15
**Description:** 

>Harambe is love. Harambe is life
http://play.spgame.site:9998
Creator - Kelvin Neo (@deathline75)

## Write-up
A simple challenge this one, we just have to view the source to figure out the logic. 

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (empty($_POST["name"])) {
            echo '<script>alert("name variable is empty!")</script>';
        } elseif (empty($_POST["comment"])) {
            echo '<script>alert("comment variable is empty!")</script>';
        } else {
            echo 'Well done, here is your flag: ';
        }
    }
    ?>

So we need to just POST `comment` and `name` variables into `index.php`.

            <div class="guestform">
            <h3>Leave your petition here</h3>
            Well done, here is your flag: GCTF{c0mm3n75_4r3_73rr1bl3_pl4c3h0ld3r5}          <h4>Someone keeps posting stupid comments, so the form is disabled for now.</h4>
                        <div>
                <div class="full-comment">
                    <div class="name">


Therefore, the flag is `GCTF{c0mm3n75_4r3_73rr1bl3_pl4c3h0ld3r5}`
