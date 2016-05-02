import datetime

time = datetime.datetime.now()
#print time
nfile = open("max", "r")
print datetime.datetime.strptime(nfile.readline().replace('\n', ''), "%d/%m/%y %H:%M")


def timestamp (name):
    nfile = open(name, 'a')
    nfile.write(time.strftime("%d/%m/%y %H:%M") + '\n')
    nfile.close()

def readtimestamp (name):
    nfile = open(name, "r")
    print nfile.read()
    nfile.close()

def timesbetween (name):
    nfile = open(name, 'r')
    lineone = nfile.readline()
    linetwo = nfile.readline()
    nfile.close()

timestamp("max")
