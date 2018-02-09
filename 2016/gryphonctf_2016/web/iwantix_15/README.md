# GryphonCTF_2016: IWanTix

**Category:** Web
**Points:** 15
**Description:**

>One of our admin really wants to watch Eason Chan's concert, but the organiser will only release their sales after 7th of November 2016. Can you help him to get the concert ticket in advance? Please..? ;_;
Play at http://play.spgame.site:9994
Creator - Chen Qiurong (@pc84560895)

## Write-up
Loading the site brings you a HTML 1.0 designed site. Horrible. Bringing up [Inspect Tools] in Google Chrome shows you that the server sends back the cookie `currentTime=1475866712`. That is unix timestamp in a nutshell, use a unix timestamp converter and get the timestamp for 8 Nov 2016, which is `1480464000`.

Afterwards, open up console and run, `document.cookie = "currentTime=1480464000"`. Following that, refresh the page. Now the page changes and you get the first half of the cookie. To get the second half, open up [Inspect Element] and deleted the `disabled` attribute on the button.

Clicking the button brings you to the other half of the cookie.

Therefore, the flag is `GCTF{cl13n751d3_v4l1d4710n_5uckz}`.
