# CSAWCTF_2017: CVV

**Category:** Misc
**Points:** 100
**Description:**

>Hey fam, you got CVV? I need some CVV!
nc misc.chal.csaw.io 8308

## Write-up
This challenge involves programming a credit card generator challenge to answer to some stupid questions. I accomplished this in [Python](solve.py).

    # ./solve.py 
    [+] Opening connection to misc.chal.csaw.io on port 8308: Done
    [*] Sending: 5112343637805266
    [*] Sending: 371442055014331
    [*] Sending: 4123458813001652
    [*] Sending: 4123455688586239
    [*] Sending: 371448875016356
    [*] Sending: 6512348578054315
    [*] Sending: 5112348402301607
    [*] Sending: 5112340363042817
    [*] Sending: 371446554844601
    [*] Sending: 6512344586486268
    [*] Sending: 5112341350115343
    [*] Sending: 5112347756607528
    [*] Sending: 6512346362448008
    [*] Sending: 5112348814205057
    [*] Sending: 5112346317537026
    [*] Sending: 4123454502483244
    [*] Sending: 5112344350131583
    [*] Sending: 6512348566784832
    [*] Sending: 371442136700072
    [*] Sending: 371440450658231
    [*] Sending: 4123456027166782
    [*] Sending: 5112347367651360
    [*] Sending: 6512343602671051
    [*] Sending: 6512348164133127
    [*] Sending: 6512340240266062
    [*] Sending: 92158080204469
    [*] Sending: 39270585531282
    [*] Sending: 66721813455179
    [*] Sending: 31020185242303
    [*] Sending: 93425046354012
    [*] Sending: 11752805382523
    [*] Sending: 68816640136634
    [*] Sending: 82052748601244
    [*] Sending: 67703873203201
    [*] Sending: 20374656483216
    [*] Sending: 41041472533863
    [*] Sending: 76804517547463
    [*] Sending: 69467384071360
    [*] Sending: 31580174680524
    [*] Sending: 66065203028158
    [*] Sending: 78780265422679
    [*] Sending: 61300788020576
    [*] Sending: 47687076568038
    [*] Sending: 97813628204810
    [*] Sending: 90593364307632
    [*] Sending: 19195522731279
    [*] Sending: 92857127367649
    [*] Sending: 25547185033371
    [*] Sending: 84935483876351
    [*] Sending: 67427422118229
    [*] Sending: 1234561204813536
    [*] Sending: 1234564068850263
    [*] Sending: 1234561464240370
    [*] Sending: 1234568383573534
    [*] Sending: 1234563707302181
    [*] Sending: 1234560437374217
    [*] Sending: 1234561133332327
    [*] Sending: 1234562888705733
    [*] Sending: 1234568287388047
    [*] Sending: 1234568852702747
    [*] Sending: 1234562562565312
    [*] Sending: 1234560442604020
    [*] Sending: 1234568786130569
    [*] Sending: 1234560864323760
    [*] Sending: 1234565186225023
    [*] Sending: 1234564422855834
    [*] Sending: 1234564074738718
    [*] Sending: 1234567716504604
    [*] Sending: 1234568746348731
    [*] Sending: 1234566077050280
    [*] Sending: 1234564015167704
    [*] Sending: 1234562028086721
    [*] Sending: 1234567812207110
    [*] Sending: 1234566500764416
    [*] Sending: 1234566206605541
    [*] Sending: 1234563052387506
    [*] Sending: 1234567504268263
    [*] Sending: 1234563873819687
    [*] Sending: 1234566703607420
    [*] Sending: 1234566700346121
    [*] Sending: 1234564773837241
    [*] Sending: 1234566188354290
    [*] Sending: 1234566072208453
    [*] Sending: 1234568750004451
    [*] Sending: 1234560726716904
    [*] Sending: 1234562583006726
    [*] Sending: 1234565604628006
    [*] Sending: 1234562685201217
    [*] Sending: 1234564032402803
    [*] Sending: 1234561401315327
    [*] Sending: 1234563637836555
    [*] Sending: 1234565868079375
    [*] Sending: 1234560508878740
    [*] Sending: 1234566614215818
    [*] Sending: 1234563314148597
    [*] Sending: 1234561671302773
    [*] Sending: 1234566122139161
    [*] Sending: 1234567235419011
    [*] Sending: 1234568640017481
    [*] Sending: 1234567707445171
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 1
    [*] Sending: 1
    [*] Sending: 0
    [*] Sending: 1
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 1
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 1
    [*] Sending: 1
    [*] Sending: 1
    [*] Sending: 0
    [*] Sending: 0
    [*] Sending: 1
    [*] Sending: 1
    [+] flag{ch3ck-exp3rian-dat3-b3for3-us3}
    [*] Closed connection to misc.chal.csaw.io port 8308

Therefore, the flag is `flag{ch3ck-exp3rian-dat3-b3for3-us3}`.
