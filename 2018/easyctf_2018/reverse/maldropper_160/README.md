# EasyCTF_2018:  Maldropper

**Category:** Reverse Engineering
**Points:** 160
**Description:**

>Mind looking at this malware dropper I found?
[File](maldrop.exe)
Note: this isn't actually malware, it just borrows obfuscation techniques from low quality malware.

## Write-up
Before I start, I would like to give a shoutout to [Keka](http://www.kekaosx.com/en/) for immediately ruining the _obfuscation_ on the hidden [binary](maldrop). By simply double-clicking, Keka automatically unzipped a [flagbuilder.exe](flagbuilder.exe).

In this case, as I was new to Windows, I looked up for the easiest tool for Windows disassembly and found [dnSpy](https://github.com/0xd4d/dnSpy). With that, we basically have the source for the flag generator. 

    using System;
    using System.Text;

    public class Test
    {
        public static void Main()
        {
            Random random = new Random(239463551);
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("easyctf{");
            for (int i = 0; i < 6; i++)
            {
                stringBuilder.Append(random.Next());
            }
            stringBuilder.Append("}");
            Console.WriteLine(stringBuilder.ToString());
        }
    }

Running this gives us our flag, literally printed right in the console.

Therefore, the flag is `easyctf{12761716281964844769159211786140015599014519771561198738372}`.
