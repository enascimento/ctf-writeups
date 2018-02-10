# HSCTF_2017: Keith and Dawg 2

**Category:** Crypto
**Points:** 200
**Description:**

>===================================================================================================
NOTE- Do Keith and Dawg 1 first.
===================================================================================================
The next day.
Keith was walking down the street, still shaken up about the events of the previous day, when a white unmarked van driving at about 80 miles per hour drove by and stopped right in front of him. Suddenly, the door slid open and five men wearing suits jumped out, grabbed Keith, and dragged him back into the van.
"Who are you?!" Keith asked.
"I'm Agent Roshan Mahanth, of the NSA," one man replied. "And we know what you've been up to."
"I...I don't know what you're talking about," Keith replied, but the sweat pouring out of his forehead gave him away.
"We also know that Jakob Degen, or Shady J Dawg, as you call him, is your 'employer', and that you two have been very busy lately. We know about the secret files Degen has. I've been undercover as Jazz Money Roshan Cash for the past two months, but I have been unable to gain access. Now, you have two options. Your first option is to cooperate with us and help us find a way to hack Degen's security measures and recover evidence that we can use against him..."
"Ok, I'll do it."
"Good. You'll hear from us soon."
Keith was then tossed out of the van. He got up and walked home, wondering how he could possibly get past Degen's security measures.
A few days later, Keith received a mysterious phone call from an unknown number. He hesitantly picked up the phone, "Mr. Keith. We have your first assignment. Go to the intersection between Quiche Street and Keif Afenue. You will find an envelope underneath the trash can. In it, you will find a flash drive with a hash we extracted associated with Jakob Degen's account on a website he frequents. Unfortunately, we do not know his password, as only the md5 hash is stored on the database. We do know, however, that Degen's keyboard is broken and only the q, w, e, r, t, and y keys are functioning. Report back when you find his password. Jazz Money out."
Keith immediately grabbed his coat and ran down Keif Afenue to the intersection with Quiche Street. Sure enough, he found an envelope with a flash drive underneath the trash can. He walked home and began work.
Find the password.
To be continued...
hash- b81b28baa97b04cf3508394d9a58caae
letters- q w e r t y 

## Write-up
Similar to the "Remember md5?" challenge of PACTF, I'm going to reuse old code!

[Solution](solve.py).

Therefore, the flag is `ywterqtwe`.