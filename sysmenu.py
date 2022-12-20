ver = 0.3
# imports
import sysdrive as sd
try:
    import os
    import msys
    import time
    import microcontroller
except Exception as lostimport:
    sd.fatalerror(1,1,lostimport)
# auto run
try:
    import autrun
except:
    print()
# app imports
try:
    import app1
    import app2
    import app3
    import app4
except Exception as error:
    sd.fatalerror(0,2,error)
# conf

my_file = open("conf.sys")
string_list = my_file.readlines()
my_file.close()
username = string_list[1]
password = string_list[3]
print(username)
pasmod = True
while pasmod:
    inp = input("password>")
    print(inp)
    if inp == password[:-1]:
        pasmod = False
    else:
        sd.fontC(1)
        print("wrong password")
        sd.fontC(0)
#main menu
sd.fontC(8)
print("micros ", ver)
print(ver)
time.sleep(2)
while 1:
    time.sleep(1)
    # theme
    sd.fontC(0)
    sd.bkg(3)
    # actual menu
    temp = msys.menu("Apps", "files", "(not done)", "restart", mname = "sysmenu")
    sd.clr()
    if temp == 1:
        temp = msys.menu("back", app1.name, app2.name, app3.name,app4.name, mname = "applications")
        if temp == 2:
            try:
                app1.main()
            except Exception as E:
                sd.clr("error: ", E)
                time.sleep(1)
        elif temp == 3:
            try:
                app2.main()
            except Exception as E:
                sd.clr("error: ", E)
                time.sleep(1)
        elif temp == 4:
            try:
                app3.main()
            except Exception as E:
                sd.clr("error: ", E)
                time.sleep(1)
        elif temp == 5:
            try:
                app4.main()
            except Exception as E:
                sd.clr("error: ", E)
                time.sleep(1)
    elif temp == 2:
        file = 1
        while file:
            temp = msys.menu("back", "list files","create and edit", mname = "files")
            if temp == 1:
                sd.clr("Good bye, going to menu")
                file = 0
            elif temp == 2:
                msys.clr(os.listdir())
                time.sleep(3)
            elif temp == 3:
                temp = 1
                sd.clr()
                import edit
                edit.main()
            else:
                sd.clr("Error")
                time.sleep(1)
    elif temp == 3:
        sd.clr("test")
    elif temp == 4:
        print("restarting...")
        microcontroller.reset()
    elif temp == 0:
        print("item not on menu")
    else:
        print("string error")

