from time import sleep
import sys


for i in range(3):
    print(i)
    sys.stdout.flush() #要這樣才會輸出到log
    sleep(1)