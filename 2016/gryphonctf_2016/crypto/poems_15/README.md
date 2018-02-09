# GryphonCTF_2016: Poems

**Category:** Cryptography
**Points:** 15
**Description:**

>This flag does not follow the GCTF{} format
Hints:
Look for patterns
Creator - Darren Ang (@Southzxc)

## Write-up
A pretty good challenge, this time around we are given a [text file](poem.txt). Using an online tool like (quipqiup)[http://quipqiup.com/], run the crack process till you get something legible. In this case, after many attempts at making sense of the poem, you get a something that sounds strange like, *if you don't get something like this, just continue matching the ciphertext with what you know are clues, like 'camaqagiax=cemeteries'*

>T there HareEcemeteries that are lonely, F grave sLfullAofG zones that do not make a sound, I the Sheart moving through a tunnel, HinO it W darkness, D darkness,Y darkness,_ like MaRshipwreck_ we die going into ourselves, TasH thoughOw eM were A drowningS inside_ our heart s,Eas D though I we S lived Of alling Nout of the skin into the soul.

Searching the phrase, `we die going into ourselves` returns a [poem](https://www.poets.org/poetsorg/poem/nothing-death). Looking further, you can then isolate the paragraph,

>There are cemeteries that are lonely,
graves full of bones that do not make a sound,
the heart moving through a tunnel,
in it darkness, darkness, darkness,
like a shipwreck we die going into ourselves,
as though we were drowning inside our hearts,
as though we lived falling out of the skin into the soul.

Does this seem very similar to the poem we are given?

If we try using the tool again, but this time around giving it clues like, `vonavy=lonely` the decoded message becomes clearer and clearer, until you are left with.

>Tthere Hare Ecemeteries that are lonely,
Fgraves Lfull Aof Gbones that do not make a sound,
Ithe Sheart moving through a tunnel,
Hin Oit Wdarkness, Ddarkness, Ydarkness,
_like Ma Rshi~wreck _we die going into ourselves,
Tas Hthough Owe Mwere Adrowning Sinside _our hearts,
Eas Dthough Iwe Slived Ofalling Nout of the skin into the soul

Take the capital letters and you get,

>THE
FLAG
IS
HOWDY
_MR_
THOMAS_
EDISON

What did you know?

Therefore, the flag is `GCTF{HOWDY_MR_THOMAS_EDISON}`
