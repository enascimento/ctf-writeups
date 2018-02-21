#! /usr/bin/env python3
##
# Created for EasyCTF 2018_RSA_v
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
import binascii
import gmpy2

# Imports courtesy of @pablocelayes
import continuedfractions
import arithmetic

# Importing variables we got
c = 7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120
n = 9247606623523847772698953161616455664821867183571218056970099751301682205123115716089486799837447397925308887976775994817175994945760278197527909621793469
e1 = 11
e2 = 41
e3 = 67623079903
e4 = 5161910578063
e5 = 175238643578591220695210061216092361657427152135258210375005373467710731238260448371371798471959129039441888531548193154205671

# Courtesy of @pablocelayes and @LFlare for reusing scripts LEL
# I'm too lazy to rebuild a library. Thanks mate.
def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = continuedfractions.rational_to_contfrac(e, n)
    convergents = continuedfractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            discr = s*s - 4*n
            if(discr>=0):
                t = arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    return d

# Calculate massive E
e = e1 * e2 * e3 * e4 * e5

# Hack d
d = hack_RSA(e, n)

# Get message
m = hex(int(pow(c, d, n)))[2:]
flag = binascii.unhexlify(m).decode()

# Print flag
print(flag)
