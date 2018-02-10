# CrossCTF_2017:

**Category:** Reverse Engineering
**Points:** 10
**Description:**

>It's trivial, my dear Watson. [File here](trivial.pyc)

## Write-up
We will be using [uncompyle2](https://github.com/wibiti/uncompyle2) to decompile the given file to result in a source [file](trivial.py). Analysing the code gives the [formula to solve this challenge.](solve.py)

Therefore, the flag is `CrossCTF{sadriain_9264656_AK4782}`.