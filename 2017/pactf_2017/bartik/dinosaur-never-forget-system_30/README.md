# PACTF_2017: Dinosaur Never-Forget System

**Category:**
**Points:** 30
**Description:**

>Those Dinosaurs…
The dinosaurs need some way to archive their messages and news for the future, so they created the Dinosaur Never-forget System. They wanted the login to be public, but they also didn’t want it to be too easy to find. So they hid it in a system more antiquated than the dinosaurs themselves.
dinosaurneverforgetsystem.tk

**Hint:**

>They kept records, too.

## Write-up
A simple challenge involving `TXT` DNS records.

    $ dig TXT dinosaurneverforgetsystem.tk

    ; <<>> DiG 9.8.3-P1 <<>> TXT dinosaurneverforgetsystem.tk
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 57478
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

    ;; QUESTION SECTION:
    ;dinosaurneverforgetsystem.tk.  IN  TXT

    ;; ANSWER SECTION:
    dinosaurneverforgetsystem.tk. 14439 IN  TXT "edger entry available at LEDGER subdomain -- flag: dinosaurs_must_stay_informed"

    ;; Query time: 347 msec
    ;; SERVER: 164.78.239.15#53(164.78.239.15)
    ;; WHEN: Tue Apr 18 13:29:49 2017
    ;; MSG SIZE  rcvd: 138

Therefore, the flag is `dinosaurs_must_stay_informed`.