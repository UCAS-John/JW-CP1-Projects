#John Wangwang RAID: Countdown Timer

import time

def countdown(t):

    while t > -1:
        mins, secs = divmod(t, 60)
        times = "{:02d}:{:02d}".format(mins, secs)
        print(times)
        time.sleep(1)
        t -= 1

def main():

    while True:
        try:
            t = int(input("Enter how long you wan your countdown timer to be(seconds): "))
            break
        except ValueError:
            print("Please enter an integer!")
            continue

    countdown(t)

    print("The timer is up!")

if __name__ == "__main__":
    main()