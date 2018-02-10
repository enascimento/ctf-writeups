# PACTF_2017: XOR 1

**Category:**
**Points:** 20
**Description:**

>My friend Miles sent me a secret message. He said he encoded it with an XOR cipher. Can you figure out what his message “KGZFK\qZFG]qA\qZFOZ” means?

**Hint:**

>The key is only one digit long

## Write-up
Given that the key is only one digit long, we can easily bruteforce this with a simple [Python script](solve.py).

    $ ./solve.py
    ...
    `lqm`wZqmlvZjwZqmdq
    gkvjgp]vjkq]mp]vjcv
    fjwkfq\wkjp\lq\wkbw
    either_this_or_that
    dhuids^uihr^ns^ui`u
    {wjv{lAjvwmAqlAjvj
    zvkwzm@kwvl@pm@kw~k
    ...

Therefore, the flag is `either_this_or_that`.