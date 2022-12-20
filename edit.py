import msys
import sysdrive as sd
import time
import storage
import os 
def main():
    sd.fontC(0)
    sd.bkg(10)
    msys.clr()
    txtlist = [""] * int(input("file length>"))
    fn = input("filename>")
    lineNum = 0
    while 1: 
        sd.clr(withreset=1)
        print("--", fn)
        inp = input(str(lineNum)+": ")
        if inp[:4] == "#go ": # used to go to diffrent line numbers
            try:
                if int(inp[4:])>-1:
                    lineNum = int(inp[4:])-1
                else:
                    print("Cant go to line ", inp[4:])
            except Exception as E:
                print(inp[4:])
                print("error: ", E)
            inp = ""
        elif inp[:4] == "#out": # prints what is written down
            inp = ""
            for i in range(len(txtlist)):
                if txtlist[i] != "": # if the string is empty dont print
                    print(str(i) + ":" + txtlist[i])
            time.sleep(2)
        elif inp[:4] == "#len": # prints length of file
            inp = ""
            print(len(txtlist))
            time.sleep(2)
        elif inp[:4] == "#run": # runs file
            inp = ""
            for i in range(len(txtlist)):
                if txtlist[i] != "": # if the line is empty dont run
                    exec(txtlist[i])
        elif inp[:4] == "#sav": # save file in write mode
            inp = ""
            storage.remount("/")
            try:
                with open(fn, 'w') as fp: 
                    for item in txtlist:
                    # write each item on a new line
                        fp.write("%s\n" % item)
                    print("done")
            except:
                print("unable to save, try eject the file drive from windows")
        txtlist[lineNum] = inp
        lineNum=lineNum+1
        time.sleep(1)
