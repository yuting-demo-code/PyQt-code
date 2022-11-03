from time import sleep
import sys


for i in range(3):
    print("嗨")
    sys.stdout.flush() #要這樣才會輸出到log
    sleep(1)