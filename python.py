# Taryn Burns
# Homework 3 Cpts 355, PYTHON

import itertools
import operator
from collections import Counter

debugging = False


def debug(*s):
    if debugging:
        print("Debugging")
        print(*s)
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# 1.
#   a. sprintLog (sprnt)
# Define a function sprintLog(sprnt) which takes a dictionary of users as shown
# above and returns a dictionary of tasks, where each task is associated with the
# users who worked on that task during the sprint. For the above dictionary, sprintLog
# will return the following:
# {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2,
# 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}}
sprnt = {} # make sprnt into an empty dictionary first

def addDict(sprnt):
    add = {}
    for i in sprnt.values():
        for j in i:
            if j in add:
                add[j] += i[j]
            else:
                add[j] = i[j]
    return add


def sprintLog(sprnt):
    user_dict = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4},
                 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1},
                 'Aaron': {'task2': 15}, 'Ethan': {'task3': 12},
                 'Helen': {'task3': 10}}
    # print(sprnt)
    return {}

#print(sprintLog(sprnt)) # prints out the return value of sprntLog()

# -----------------------------------------------------------------------
#  b. addSprints(sprint1, sprint2)
# Now define a function, addSprints(sprint1, sprint2), which takes the logs of two
# sprints as input and joins them. The result will be a joined dictionary including
# tasks from both dictionaries. The logs for the tasks that are common to both
# dictionaries will be merged. See below for an example
sprint1 = {}
sprint2 = {}

def addSprints(sprint1, sprint2):
    mergedsprint = {}
    sprint1 = Counter({'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11},
               'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3':
               {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}})
    sprint2 = Counter({'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2':
               {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4':
               {'Helen': 16}})
    mergedsprint = sprint1 + sprint2
    mergedsprint.update(sprint2)
    print(mergedsprint)



# -----------------------------------------------------------------------
#  c. addNLogs (logList)
# Now assume that the team recorded the log data for several sprints as a list
# of dictionaries. This list includes a dictionary for each development sprint.
# Define a function addNLogs which takes a list of developer sprint logs and
# returns a dictionary which includes the collection of all project tasks and the
# total number of hours each developer has worked on each task. Your function definition
# should use the Python map and reduce functions as well as the sprintLog and addSprints
# functions you defined in part(a) and (b).

def addNLogs(logList):
    pass


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# 2.
#  a. lookupVal(L,k)
# Write a function lookupVal that takes a list of dictionaries L and a key k as input
# and checks each dictionary in L starting from the end of the list. If k appears in
# a dictionary, lookupVal returns the value for key k. If k appears in more than one
# dictionary, it will return the one that it finds first (closer to the end of the list).
L1 = [{"x": 1, "y": True, "z": "found"}, {"x": 2}, {"y": False}]


def lookupVal(L, k):
    for m in reversed(L1):
        for key in m:
            if key == k:
                return m[key]


# -----------------------------------------------------------------------
#  b. lookupVal2 (tL, k)
# Write a function lookupVal2 that takes a list of tuples (tL) and a key k as input.
# Each tuple in the input list includes an integer index value and a dictionary. The
# index in each tuple represent a link to another tuple in the list (e.g. index 3 refers
# to the 4th tuple, i.e., the tuple at index 3 in the list)  lookupVal2 checks the
# dictionary in each tuple in tL starting from the end of the list and following the
# indexes specified in the tuples.
L2 = [(0, {"x": 0, "y": True, "z": "zero"}),
      (0, {"x": 1}),
      (1, {"y": False}),
      (1, {"x": 3, "z": "three"}),
      (2, {})]


def indexhelp(i, tL, k):
    if k in tL[i][1]:
        # if wanted key is current dic tuple, return value
        return tL[i][1][k]
    elif i != 0:
        i = tL[i][0]
        # recursively call funct when we're not on 1st tuple in dict list
        return indexhelp(i, tL, k)
    elif i == 0:
        if k in tL[i][1]:
            # if on 1st typle in list, either return value
            return tL[i][1][k]
        else:  # or return none
            return None
    else:
        # if fails, return none
        return None


def lookupVal2(tL, k):
    # we will be starting at the back of the list
    # since we are already using i, in order to not get confused with the other
    # i we have in the index help funct, we will replace i with index in this function
    index = -1
    return indexhelp(index, tL, k)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# 3. unzip
# Write a function unzip that calculates the reverse of the zip operation. unzip
# takes a list of 3tuples, L, as input and returns a tuple of lists, where each
# list includes the first, second, or third element from each tuple, respectively.
# Give a solution using higher order functions (map, reduce or filter), without using
# loops.
# For example: unzip ([(1,"a",{1:"a"}),(2,"b",{2:"b"}),(3,"c",{3:"c"}),(4,"d",{4:"d"})])
# returns([1, 2, 3, 4], ['a', 'b', 'c', 'd'], [{1: 'a'}, {2: 'b'}, {3: 'c'}, {4: 'd'}])

def unzip():
    l1 = ([(1, "a", {1: "a"}), (2, "b", {2: "b"}), (3, "c", {3: "c"}), (4, "d", {4: "d"})])
    unzippedlist = tuple(map(list, zip(*l1)))
    # print(unzippedlist) # prints out unziped
    return unzippedlist


# prints out returned value from unzip() func
# print(unzip())

#  next two lines is the short way but prints out the same
# tuplelist = ([(1,"a",{1:"a"}),(2,"b",{2:"b"}),(3,"c",{3:"c"}),(4,"d",{4:"d"})])
# list(zip(*tuplelist))
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# 4. numPaths(m,n,blocks)
# Consider a robot in a mXn grid who is only capable of moving right or
# down in the grid (can’t move left, up or diagonal). The robot starts at
# the top left corner, (1,1), and is supposed to reach to the bottom right
# corner: (m,n). Some of the cells in the grid are blocked and the robot is
# not allowed to visit those cells. Write a function numPaths that takes the
# grid length and width (i.e., m,n) and the list of the blocked cells (blocks)
# as argument and returns the number of different paths the robot can take from
# the start to the end. Give and answer using recursion. (A correct solution
# without recursion will be worth half the points.)

def positionIsBlocked(position, blocks):
    if (position[0] > 0 and position[1] > 0):
        if not position in blocks:
            return True  # if the position is not blocked and it is not outside of the grid return True
    else:
        return False  # otherwise return false


def numPaths(m, n, blocks):
    position = (m, n)  # sets the position
    paths = 0  # keeps track of path numbers
    if positionIsBlocked((position[0] - 1, position[1]), blocks):
        paths += numPaths(position[0] - 1, position[1],
                          blocks)  # if this passes the positionIsBlocked condition with the new position, recursively call with adjusted m
    if positionIsBlocked((position[0], position[1] - 1), blocks):
        paths += numPaths(position[0], position[1] - 1,
                          blocks)  ##if this passes the positionIsBlocked condition with the new position, recursively call with adjusted n
    if position == (1, 1):
        return 1  # if we reach the finish return 1 for paths
    return paths  # return number of paths


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# 5.
#   a. iterFile()
# Create an iterator that represents the sequence of words read from a
# text file. The iterator is initialized with the name of the file and
# the iterator will return the next word from the file for each call to
# __next__(). The iterator should ignore all empty lines and end of line
# characters.  A sample input file ("testfile.txt") is attached.

def iterFile():
    # want to open the file
    with open('testfile.txt0', 'r') as file:
        data = file.read()


# -----------------------------------------------------------------------
#   b. wordHistogram(words)
# Define a function wordHistogram that takes an iterator “words” (representing a
# sequence of words) and builds histogram showing how many times each word appears in the
# file. wordHistogram should return a list of tuples, where each tuple includes a unique
# word and the number of times that word appears in the file.
def wordHistogram(words):
    histotable = dict()
    for char in words:
        if histotable.get(char) : histotable[char] += 1
        else : histotable[char] = 1
    histolist = histotable.items()
    histolist = sorted(histolist)
    histolist = sorted(histolist, key=lambda x: x[1], reverse=True)
    return histolist


# my own lil test for histogram, runs with no issue without implementing in iter()
def testhisto():
    test = "implemented"
    answer = [('-', 5), ('CptS', 3), ('355', 3), ('Assignment', 3), ('3', 3), ('Python', 3), ('Warmup', 3), ('text', 2),
              ('for', 2), ('This', 1), ('is', 1), ('a', 1), ('test', 1), ('file', 1), ('With', 1), ('some', 1),
              ('repeated', 1), ('.', 1)]
    if wordHistogram(test) != answer:
        return False
    else:
        return True
    return True
# -----------------------------------------------------------------------
# my own lil test functions in order to see if they're working
# -----------------------------------------------------------------------
def testnumPaths():
    if numPaths(2, 2, [(2, 1)]) != 1:
        return False
    if numPaths(3, 3, [(2, 3)]) != 3:
        return False
    if numPaths(4, 3, [(2, 2)]) != 4:
        return False
    if numPaths(10, 3, [(2, 2), (7, 1)]) != 27:
        return False
    return True


def testlookupVal():
    L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]

    if lookupVal(L1,"x") != 2:
        return False
    if lookupVal(L1,"y") != False:
        return False
    if lookupVal(L1,"z") != "found":
        return False
    if lookupVal(L1,"t") != None:
        return False
    return True

def testlookupVal2():
    L2 = [(0,{"x":0,"y":True,"z":"zero"}),
        (0,{"x":1}),
        (1,{"y":False}),
        (1,{"x":3, "z":"three"}),
        (2,{})]

    if lookupVal2(L2,"x") != 1:
        return False
    if lookupVal2(L2,"y") != False:
        return False
    if lookupVal2(L2,"z") != "zero":
        return False
    if lookupVal2(L2,"t") != None:
        return False
    return True

def testsprintlog():
    sprint = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4},
                 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1},
                 'Aaron': {'task2': 15}, 'Ethan': {'task3': 12},
                 'Helen': {'task3': 10}}
    if sprintLog(sprint) == ({'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4},
                 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1},
                 'Aaron': {'task2': 15}, 'Ethan': {'task3': 12},
                 'Helen': {'task3': 10}}):
        return True
    else:
        return False

if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    if testnumPaths():
        print(passedMsg % '*testnumpaths')
        print("(2,2,[(2,1)]) returns 1 ")
        print("(3,3,[(2,3)]) returns 3 ")
        print("(4,3,[(2,2)]) returns 4 ")
        print("(10,3,[(2,2),(7,1)]) returns 27 ")
    else:
        print(failedMsg % '*testnumPaths')
    if testhisto():
        print(passedMsg % '*testhisto')
    else:
        print(failedMsg % '*testhisto')
    if testlookupVal():
        print(passedMsg % '*lookupVal')
        print("(L1,'x') returns 2")
        print("(L1,'y') returns False")
        print("(L1,'z') returns 'found' ")
        print("(L1, 't') returns none")
    else:
        print(failedMsg % '*lookupVal')
    if testlookupVal2():
        print(passedMsg % '*lookupVal2')
        print("(L2,'x') returns 1")
        print("(L2,'y') returns False")
        print("(L2,'z') returns 'zero' ")
        print("(L2, 't') returns none")
    else:
        print(failedMsg % '*lookupVal2')
    if testsprintlog():
        print(passedMsg % '*sprintlog')
    else:
        print(failedMsg % '*sprintlog')


