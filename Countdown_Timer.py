import time

def countdown(t):

    while t:
        mins,sec=divmod(t,60)
        start_timer = '{:02d}:{:02d}'.format(mins, sec)
        print(start_timer,end="\r")
        time.sleep(1)
        t -= 1
    print('countdown ends')

t=input('Enter the countdown in secounds : ')

countdown(int(t))
