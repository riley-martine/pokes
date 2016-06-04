#!/usr/bin/env python
"""analytics for fb pokes."""

import datetime  # need for time
import os.path  # need for file creation


TIME = datetime.datetime.now()  # get current time as object
NAME = raw_input("name: ")  # get name of person you are interacting with

if not os.path.isfile(NAME):  # if there is not already a file for this person
    # check if they typed the wrong name
    if raw_input("is the name \"" + NAME + "\" correct? (y/n): ") == "y":
        print "creating file..."
        # if they typed the right name let them know whats up
        FILECREATE = open(NAME, 'w+')  # make a new file
        FILECREATE.close()
        # close it bc we need to open it appendingly later anyways
        print "done creating file"  # tell them you completed successfully
    else:  # if they typed the wrong name
        exit()  # exit program

NFILE = open(NAME, "r+")  # open namefile (nfile) by name with read permissions
NFILEEDIT = open(NAME, "a+")  # open nfile for editing in append mode
LINES = NFILE.readlines()  # make a nice list of all the lines in order


THEYGLOBAL = 0  # we need this in a sec

if LINES != []:  # if lines isn't blank
    if LINES[0][0] == "t":  # and if it starts with "they start"
        THEYGLOBAL = 1  # let the code down below know they started
    del LINES[0]  # from our temporary list remove that line
else:  # if lines is not blank
    if raw_input("who poked last? t/y: ") == "t":
        # ask who poked last, if it was them
        NFILEEDIT.write("they start\n")  # write to file they started
    else:  # if it was you
        NFILEEDIT.write("you start\n")  # write you start


def timestamp():
    """stamp current time."""
    # write to file current time formatted nicely
    NFILEEDIT.write(TIME.strftime("%d/%m/%y %H:%M:%S") + '\n')


def customtimestamp(inputtime):
    """write time given."""
    # given inputtime write inputtime to file
    NFILEEDIT.write(TIME.strftime(inputtime) + '\n')


def getline(linenum):
    """Grab line time as dt obj."""
    # get the line (do not question this code)
    return datetime.datetime.strptime(
        LINES[linenum].replace('\n', ''), "%d/%m/%y %H:%M:%S")


def timesbetween(init, follow):
    """subtract datetime objects from each other."""
    return getline(follow) - getline(init)


def alltimesbetween():
    """get all times in between pokes, with person who did thing appended."""
    plist = []  # initialize paired list (I know these aren't really plists)
    they = THEYGLOBAL
    for i in range(1, len(LINES)):
        plist1 = []
        if they == 0:  # if they did not start, then you did
            # if you started, the first wait was from your press to their
            # press, thus the time they waited to press is this
            plist1.append("they waited")
            they = 1  # switch it up bb
        elif they == 1:  # the opposite of that
            plist1.append('you waited ')  # ye do this
            they = 0
        plist1.append(str(timesbetween(i - 1, i)))  # append to temp plist
        # append to the other set of indecies so we have list of lists
        plist.append(plist1)
        plist1 = []  # set temp plist blank
    return plist  # return list of lists


def split(plist):
    """print every other index in list, then print the rest."""
    plist1 = []  # init blank list
    count = 0  # bool count for passes
    for i in plist:  # for every ime between
        if count == 0:  # if even pass
            print i  # print the thing
            count = 1  # xor count
        elif count == 1:  # if odd pass
            plist1.append(i)  # save to print later
            count = 0  # xor count
    for i in plist1:  # for everything not printed
        print i  # print it


def averageall():
    """average of all waits."""
    sumtime = datetime.timedelta()
    for i in range(1, len(LINES)):
        sumtime += timesbetween(i - 1, i)
    print sumtime / len(LINES)


def average():
    """average times by person."""
    youdate = datetime.timedelta()
    younum = 0
    theydate = datetime.timedelta()
    theynum = 0
    they = THEYGLOBAL
    for i in range(1, len(LINES)):
        if they == 0:
            theydate += timesbetween(i - 1, i)
            theynum += 1
            they = 1  # switch it up bb
        elif they == 1:  # the opposite of that
            youdate += timesbetween(i - 1, i)
            younum += 1
            they = 0
    print "\ntheir average"
    print theydate / theynum
    print "\nyour average"
    print youdate / younum


def main():
    """select mode."""
    mode = raw_input(
        "Mode? (stamp, cstamp, read, split, averageall, average, or quit): ")
    if mode == "stamp":  # if asked to timestamp now
        timestamp()  # do that
	main()
    elif mode == "cstamp":  # if you missed the last time to timestamp
        # prompt for timestamp and then add it
        customtimestamp(raw_input("time in form " +
                                  TIME.strftime("%d/%m/%y %H:%M:%S") + ": "))
	main()
    elif mode == "read":  # if you want to know the times between
        for i in alltimesbetween():  # get all times between
            print i  # print them
	main()
    elif mode == "split":  # if you want times waited organized by person
        split(alltimesbetween())
	main()  # split all times between
    elif mode == "quit":  # if you type q
        exit()  # exit
    elif mode == "averageall":
        averageall()
	main()
    elif mode == "average":
        average()
	main()
    else:  # if you made a typo
        print "That's not a mode"  # let you know
        main()  # retry mode selector (main)

main()  # this is what gets executed

NFILEEDIT.close()  # close edit file
NFILE.close()  # close read name file
