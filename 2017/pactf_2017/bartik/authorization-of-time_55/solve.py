#! /usr/bin/env python
##
# Created for the Authorization Of Time challenge
# By Amos Ng
##
import pyotp

totp =  pyotp.TOTP("ORUW2ZK7OBQXG43FONPWE5LUL5RXK2LMONPXG5DBPFPXI2DFL5ZWC3LF")
otp = totp.at(1489798809)

print("Flag: %s" % otp)