import time

def testtimer(sec, test):
    while True:
        print("Waiting", sec, "Note:", test)
        time.sleep(sec)

testtimer(3, "This is a test")