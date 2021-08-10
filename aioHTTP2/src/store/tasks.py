
def init():
    global myList
    global myDict
    myList = []
    myDict = {}

def addItem(item):
    global myList
    myList.append(item)

def getItem():
    global myList
    return(myList)