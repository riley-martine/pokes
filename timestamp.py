import datetime
import os.path



time = datetime.datetime.now()
name = raw_input("name:")

if not os.path.isfile(name):
    if raw_input("is the name \"" + name + "\" correct? (y/n): ") == "y":
        print "creating file..."
        file = open(name, 'w+')
        file.close()
        print "done creating file"
    else:
        exit()

nfile = open(name, "r+")
nfileedit = open(name, "a+")
lines = nfile.readlines()


they = 0

if lines != []:
    if lines [0][0] == "t":
        they = 1
    del lines[0]
else:
    if raw_input("who poked last? t/y: ") == "t":
        nfileedit.write("they start\n")
    else:
        nfileedit.write("you start\n")

def timestamp():
    nfileedit.write(time.strftime("%d/%m/%y %H:%M:%S") + '\n')
def customtimestamp(inputtime):
    nfileedit.write(time.strftime(inputtime) + '\n')
def getline (linenum):
    return datetime.datetime.strptime(lines[linenum].replace('\n', ''), "%d/%m/%y %H:%M:%S")
def timesbetween(init, follow):
    return getline(follow) - getline(init)
def alltimesbetween():
    plist = []
    you = 1 # init at your press
    count = 0
    for i in range (1, len(lines)):
        plist1 = []
        if you == 1:
            plist1.append("they waited")
            you = 0
        elif you == 0:
            plist1.append('you waited ')
            you = 1
        plist1.append(str(timesbetween(i-1, i)))
        plist.append(plist1)
        plist1 = []
    return plist
def split(plist):
    plist1 = []
    count = 0
    if they == 1:
        count = 1
    for i in plist:
        if count == 0:
            print i
            count = 1
        elif count == 1:
            plist1.append(i)
            count = 0
    for i in plist1:
        print i

def main():
    mode = raw_input("Mode? (stamp, cstamp, read, or split: ")
    if mode == "stamp":
        timestamp()
    elif mode == "cstamp":
        customtimestamp(raw_input("time in form " + time.strftime("%d/%m/%y %H:%M:%S") + ": ") + '\n')
    elif mode == "read":
        for i in alltimesbetween():
            print i
    elif mode == "split":
        split(alltimesbetween())
    elif mode =="q":
        exit()
    else:
        main()

main()

nfileedit.close()
nfile.close()
