name = "cmd"
from sysdrive import fontC
from sysdrive import bkg
from sysdrive import clr
import microcontroller
def info():
    fontC(8)
    print("To exit type exit() ")
    print("To get help type help() ")
    fontC(0)
def exit():
    py = 0
    microcontroller.reset()
def main():
    fontC(0)
    bkg(10)
    clr()
    py = 1
    print("cmd python shell")
    print("running on ", __name__)
    while py:
        inp = input("py>")
        try:
            if inp == "exit":
                    fontC(8)
                    print("INFO: To exit type exit() ")
                    fontC(0)
            elif inp == "help":
                    fontC(8)
                    print("INFO: To get help type help() ")
                    fontC(0)
            else:
                exec(inp)
        except Exception as ERROR:
            fontC(1)
            print ("Error: ", ERROR)
            fontC(0)