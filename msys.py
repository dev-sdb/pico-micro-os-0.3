import sysdrive # critical system functions
def menu(*mitem, mname): # menu
    sysdrive.clr()
    cnt = 0
    print("---", mname) # displays menu name
    for i in mitem: # displays menu items
        cnt = cnt+1
        print(cnt,"-",i)
    try: # checks for string error
        for i in range(0,24-cnt-2):
            print()
        usr_inp = int(input(">")) # gets input
    except:
        return -1
    if usr_inp < 1 or usr_inp > cnt: # checks if items on menu
        return 0
    return usr_inp
def clr(withtext=""):
    for i in range(0,23):
        print() #clear screen
    print(withtext)
