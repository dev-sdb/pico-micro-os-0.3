ver = 0.2
import time


# --------------- display drivers

# ------------ text colour

def font(mode, state, extra = 0):
    if mode == 1: # boldness
        if state:
            print("\033[1m")
        else:
            print("\033[21m")
    elif mode == 2: # clear line
        print("\033[2k")
        print()
    elif mode == 3: # underline
        if state:
            print("\033[4m")
        else:
            print("\033[24m")
def fontC(colour):
    if colour == 0: # white
        print("\033[38;2;255;255;255m")
    elif colour == 1: # red
        print("\033[38;2;255;0;0m")
    elif colour == 2: # green
        print("\033[38;2;0;255;0m")
    elif colour == 3: # blue
        print("\033[38;2;0;0;255m")
    elif colour == 4: # darkred
        print("\033[38;2;125;0;0m")
    elif colour == 5: # darkgreen
        print("\033[38;2;0;125;0m")
    elif colour == 6: # darkblue
        print("\033[38;2;0;0;125m")
    elif colour == 7: # cyan
        print("\033[38;2;125;255;255m")
    elif colour == 8: # yellow
        print("\033[38;2;255;255;0m")
    elif colour == 9: # dark yellow
        print("\033[38;2;125;125;0m")
    elif colour == 10: # black
        print("\033[48;2;0;0;0m")

# --------------- background colours

def bkg(colour):
    if colour == 0: # white
        print("\033[48;2;255;255;255m")
    elif colour == 1: # red
        print("\033[48;2;255;0;0m")
    elif colour == 2: # green
        print("\033[48;2;0;255;0m")
    elif colour == 3: # blue
        print("\033[48;2;0;0;255m")
    elif colour == 4: # darkred
        print("\033[48;2;125;0;0m")
    elif colour == 5: # darkgreen
        print("\033[48;2;0;125;0m")
    elif colour == 6: # darkblue
        print("\033[48;2;0;0;125m")
    elif colour == 7: # cyan
        print("\033[48;2;125;255;255m")
    elif colour == 8: # yellow
        print("\033[48;2;255;255;0m")
    elif colour == 9: # dark yellow
        print("\033[48;2;125;125;0m")
    elif colour == 10: # black
        print("\033[48;2;0;0;0m")
# ------------ clear screen

def clr(withtext="", withreset=1):
    for i in range(0,50):
        print() #clear screen
    if withreset:
        print("\033[H")
    print(withtext)



# --------------- critical system functions



def fatalerror(errtype = 0, errcode = 0, mesg = "undefined"):
    bkg(4)
    fontC(1)
    print("----------------------ERROR---------------------")
    if errtype == 1:
        print("errtype: boot error")
        print("errcode: ", errcode)
        print("mesg: ", mesg)
        for i in range(0,19): # puts text at top of screen
            print()
        while 1:
            time.sleep(1)
    elif errtype == 0:
        print("errtype: fatal error")
        print("errcode: ", errcode)
        print("mesg: ", mesg)
        for i in range(0,19): # puts text at top of screen
            print()
        while 1:
            time.sleep(1)
    else:
        print("errtype: halt")
        print("errcode: ", errcode)
        print("mesg: ", mesg)
        for i in range(0,19): # puts text at top of screen
            print()
        while 1:
            time.sleep(1)
def restart():
    print("restarting...")
    machine.reset()
time.sleep(1) # gives time for serial to catch up
