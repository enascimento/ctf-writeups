# AngstromCTF_2018: Waldo 2

**Category:** Misc
**Points:** 30
**Description:**

>Now I have to find the [Waldo among the Waldos](waldo.zip)! Man, if I looked at these 1 per 5 seconds, it would take me 42 minutes to find the odd man out. There must be a better way...

## Write-up
We find the unique jpeg, only to find out it's not a jpeg.

    # md5sum * | sort -u -t' ' -k1,1
    9f6e902c233020026caf0ebbb1cf0ff5  waldo339.jpg
    ea7368fe0412bfa60cd5baf6a5c13fc9  waldo100.jpg
    # file waldo339.jpg 
    waldo339.jpg: ASCII text
    # cat waldo339.jpg 
    actf{r3d_4nd_wh1t3_str1p3s}

Therefore, the flag is `actf{r3d_4nd_wh1t3_str1p3s}`.
