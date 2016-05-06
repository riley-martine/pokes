import datetime #need for time
import os.path  #need for file creation


time = datetime.datetime.now()  #get current time as object
name = raw_input("name: ")      #get name of person you are interacting with

if not os.path.isfile(name):    #if there is not already a file for this person
    if raw_input("is the name \"" + name + "\" correct? (y/n): ") == "y":  #check if they typed the wrong name
        print "creating file..."    #if they typed the right name let them know whats up
        file = open(name, 'w+')     #make a new file
        file.close()                #close it bc we need to open it appendingly later anyways
        print "done creating file"  #tell them you completed successfully
    else:           #if they typed the wrong name
        exit()      #exit program

nfile = open(name, "r+")       #open namefile (nfile) by name with read permissions
nfileedit = open(name, "a+")   #open nfile for editing in append mode
lines = nfile.readlines()      #make a nice list of all the lines in order


theyglobal = 0       #we need this in a sec

if lines != []:      #if lines isn't blank
    if lines [0][0] == "t":  #and if it starts with "they start"
        theyglobal = 1      #let the code down below know they started
    del lines[0]      #from our temporary list remove that line
else:    #if lines is not blank
    if raw_input("who poked last? t/y: ") == "t":    #ask who poked last, if it was them
        nfileedit.write("they start\n")              #write to file they started
    else:              #if it was you
        nfileedit.write("you start\n")               #write you start

def timestamp():
    nfileedit.write(time.strftime("%d/%m/%y %H:%M:%S") + '\n')   #write to file current time formatted nicely

def customtimestamp(inputtime):
    nfileedit.write(time.strftime(inputtime) + '\n') #given inputtime write inputtime to file

def getline (linenum):
    return datetime.datetime.strptime(lines[linenum].replace('\n', ''), "%d/%m/%y %H:%M:%S") #get the line (do not question this code)

def timesbetween(init, follow):
    return getline(follow) - getline(init)  #subtract datetime objects from each other

def alltimesbetween():    #get all times in between pokes, with person who did thing appended
    plist = []      #initialize paired list (I know these aren't really plists)
    count = 0
    they = theyglobal
    for i in range (1, len(lines)):
        plist1 = []
        if they == 0: #if they did not start, then you did
            plist1.append("they waited") #if you started, the first wait was from your press to their press, thus the time they waited to press is this
            they = 1 #switch it up bb
        elif they == 1:       #the opposite of that
            plist1.append('you waited ')   #ye do this
            they = 0
        plist1.append(str(timesbetween(i-1, i)))   #append to temp plist
        plist.append(plist1) #append to the other set of indecies so we have list of lists
        plist1 = [] #set temp plist blank
    return plist   #return list of lists

def split(plist):       #print every other index in list, then print the rest
    plist1 = []         #init blank list
    count = 0           #bool count for passes
    for i in plist:     #for every ime between
        if count == 0:  #if even pass
            print i     #print the thing
            count = 1   #xor count
        elif count == 1:#if odd pass
            plist1.append(i)#save to print later
            count = 0   #xor count
    for i in plist1:    #for everything not printed
        print i         #print it

def main():
    mode = raw_input("Mode? (stamp, cstamp, read, or split: ") #ask for mode
    if mode == "stamp": #if asked to timestamp now
        timestamp()     #do that
    elif mode == "cstamp": #if you missed the last time to timestamp
        customtimestamp(raw_input("time in form " + time.strftime("%d/%m/%y %H:%M:%S") + ": ") + '\n') #prompt for timestamp and then add it
    elif mode == "read": #if you want to know the times between
        for i in alltimesbetween(): #get all times between
            print i      #print them
    elif mode == "split": #if you want times waited organized by person
        split(alltimesbetween()) #split all times between
    elif mode =="q":    #if you type q
        exit() #exit
    else:      #if you made a typo
        print "That's not a mode" #let you know
        main() #retry mode selector (main)

main()  #this is what gets executed

nfileedit.close() #close edit file
nfile.close()     #close read name file
