# CrossCTF_2017: GovTech Binary Challenge Level 1

**Category:** Binary
**Points:** 75
**Description:**

>I wonder what's happening in the class  les! I have been waiting a really long time for this... [File here](dist.zip)

## Write-up
This is a relatively simple challenge easily solvable through tools like JD-GUI. The flag for the first challenge is embedded in `Main.class` and can be seen using `$ strings Main.class`

    $ strings finals/govtech-binary-challenge-level-1_75/dist/Main.class 
    flag1
    Ljava/lang/String;
    <init>
    Code
    LineNumberTable
    main
    ([Ljava/lang/String;)V
    <clinit>
    SourceFile
    Main.java

    'flag1{7171a60f8cf4a789b7fa5906aa78f3e7}
    Main
    java/lang/Object
    xctf/NothingImportant
    march_on
    (Ljava/lang/String;)V

Therefore, the flag is `flag1{7171a60f8cf4a789b7fa5906aa78f3e7}`.
