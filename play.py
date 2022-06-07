import time
import os

def clear():
	os.system("clr" if os.name == "nt" else "clear")

while True:
    clear()
    time.sleep(3)
    print(("      *      \n") + ("| ^ ^ ^ ^ ^ |\n") + ("|^ ^ ^ ^ ^ ^|\n") + ("| ^ ^ ^ ^ ^ |\n") +("|1|2 |3| 2|1|\n"))
    time.sleep(1)
    clear()
    print(("| ^ ^*^ ^ ^ |\n") + ("|^ ^ ^ ^ ^ ^|\n") + ("| ^ ^ ^ ^ ^ |\n") + ("|1|2 |3| 2|1|\n"))
    time.sleep(1)
    clear()
    print(("| ^ ^ ^ ^ ^ |\n") + ("|^ ^ ^*^ ^ ^|\n") + ("| ^ ^ ^ ^ ^ |\n") + ("|1|2 |3| 2|1|\n"))
    time.sleep(1)
    clear()
    print(("| ^ ^ ^ ^ ^ |\n") + ("|^ ^ ^ ^ ^ ^|\n") + ("| ^ ^*^ ^ ^ |\n") + ("|1|2 |3| 2|1|\n"))
    time.sleep(1)
    clear()
    print(("| ^ ^ ^ ^ ^ |\n") + ("|^ ^ ^ ^ ^ ^|\n") + ("| ^ ^ ^ ^ ^ |\n") +("|1|2*|3| 2|1|\n"))
    time.sleep(10)
    break
