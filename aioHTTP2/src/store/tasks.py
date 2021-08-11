
def init(): 
    global myList
    global myDict   
    myList = []
    myDict = {}

def addItem(item):
    if item not in myDict:
        myList.append(item)
        myDict[item] = "something"
   
def getItem():
    print(myDict)
    return(myList)