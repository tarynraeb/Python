
# taryn burns
# interpreter ssps


import re
import sys

import itertools
import operator
from collections import Counter


debug_level = 0
helper_dictionary = {}
# debugging func so that we can print errors in our code
def debug(*s):
    if debug_level > 0:
        print(s)

        
opstack = []  # assuming top of the stack is the end of the list


# Now define the helper functions to push and pop values on the opstack
# (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

# pops cvalue from opstack
def opPop():
    if (len(opstack) > 0):
        return opstack.pop()
    else:
        print("No values in the operand (op) stack")
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

# pushes value onto opstack
def opPush(value):
    opstack.append(value)

# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.

# The dictionary stack

dictstack = []

# pops value off of dict stack
def dictPop():
    if (len(dictstack) > 0):
        return dictstack.pop()
    else:
        print("No dictionaries in dictionary stack")

# dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)



    # add name:value pair to the top dictionary in the dictionary stack.
    # Keep the '/' in the name constant.
    # Your psDef function should pop the name and value from operand stack and, call define
# defines name and a value to the dictstack
def define(name, value):
    if not dictstack:
        dictionary = dict()
        dictionary[name] = value
        #changed define to push a tuple
        dictPush((0, dictionary))

    else:
        (dictstack[-1][1])[name] = value

scope = ""


# whats design decision about what to do when theres no defn for name if name isnt defind
# your program should not break, but should give an appropriate error message.
# looks up name in dictstack
def lookup(name, scope):
    actualName = '/' + name
    revd = reversed(dictstack)

    if (scope == 'dynamic'):
        for item in revd:
            (index, dictionary) = item

            if (actualName in dictionary):
                return (index, dictionary[actualName])

        else:
            return None

    elif (scope == 'static'):
        index = len(dictstack) - 1
        dictionary = list(dictstack)

        return staticRecursion(dictionary, actualName, index)


def staticRecursion(sDict, sName, sIndex):
    #if name is found return dict and index
    if (sName in dictstack[sIndex][1]):
        return (sIndex, dictstack[sIndex][1][sName])
    #if end of index return none
    elif (sIndex == dictstack[sIndex][0]):
        return None
    #otherwise iterate through
    else:
        next, _ = dictstack[sIndex]
        _ = sDict.pop(sIndex)
        return staticRecursion(sDict, sName, next)

# Arithmetic and comparison operators
def add():
    if (len(opstack) >= 2):
        # pop top value off the op stack
        op1 = float(opPop())
        # pop the top value off op stack
        op2 = float(opPop())
        # add the two operand stacks together into a new stack
        newoperandstack = op1 + op2
        opPush(newoperandstack)  # values of op1 and op2 pushed onto the new op stack
    else:
        print("Don't have more than one parameter in stack, so we can't add. Need"
              "more parameters in the operand stack.")

# subtracts values in the stack
def sub():
    if (len(opstack) >= 2):
        op1 = float(opPop())  # pop top value off of op1
        op2 = float(opPop())  # pop top value off of op2
        newoperandstack = op2 - op1  # we subtract since we're in the subtract func
        opPush(newoperandstack)  # push values of op1 and op2 onto new op stack
    else:
        print("Can't subtract. There is not enough parameters in order for it to run properly.")
    print("Not enough parameters in operand stack for sub")

# multiplies the values in the opstack
def mul():
    if (len(opstack) >= 2):
        op1 = float(opPop())
        op2 = float(opPop())
        newoperandstack = op1 * op2  # since we're multiplying we can technically use any order
        # push op1 * op2 onto the new stack
        opPush(newoperandstack)
    else:
        print("Cannot fulfil multiply function. Need more than one parameter.")

def div():
    if (len(opstack) >= 2):
        op1 = opPop() # pop the top value off the operand stack
        op2 = opPop() # pop the top value off the operand stack

        opNew = op2 / op1
        opPush(opNew) # push (op1 / op2) onto the operand stack
       
    else:
        print("Not enough parameters in operand stack for div")

# checks to see if values are equal to each other
def eq():
    op1 = opPop()
    op2 = opPop()
    opPush(op1 == op2)

# checks to see if value op1 is less than op2
def lt():
     op1 = opPop()
     op2 = opPop()
     # pushes only if op1 < op2
     opPush(op1 > op2)

# checks to see if one value op1 is greater than op2
def gt():
    op1 = opPop()
    op2 = opPop()
    opPush(op1 < op2)  # push true if op1 > op2

#--------------------------- 15% -------------------------------------
# Array operators: define the array operators length, get

def length():
    if (len(opstack) > 0):
        op = opPop()
        if (type(op) == list):
            opPush(len(op))
        else:
            opPush(op)

def get():
    if (len(opstack) > 0):
        num = opPop()
        currList = opPop()
        if (type(num) == int and type(currList) == list):
                opPush(currList[num])
        else:
            opPush(currList)
            opPush(num)
            print("First value popped not an int or Second value popped not a list")
    else:
        print("Op stack is empty for get()")

# stores any as array[index]
def put():
    templist = [5,6,7,8,9,10]
    # print(templist)
    templist[3] = 1
    opPush(templist)
    # print(templist)
    # temp = {}
    # op = opPop()
    # temp[2] = 3
    # opPush(temp)

# pushes the array onto the stack
def aload():
    array_stack = {}
    array_stack.append(5, 4, 7, 8, 9)

# bool operators

def psAnd():
    op1 = opPop()
    op2 = opPop()
    if (op1 == True and op2 == True):
        opPush(True)
    else:
        opPush(False)

def psOr():
    op1 = opPop()
    op2 = opPop()
    if (op1 == True and op2 == False):
        opPush(True)
    elif (op1 == False and op2 == True):
        opPush(True)
    else:
        opPush(False)

def psNot():
    op = opPop()
    if (op == True):
        opPush(False)
    elif (op == False):
        opPush(True)


# stack manipulation and print operators

def dup():
    op = opPop()
    opPush(op)
    opPush(op)

def exch():
    op1 = opPop()
    op2 = opPop()
    opPush(op1)
    opPush(op2)

def pop():
    opPop()

def copy():
    index = opPop()
    try:
        for i in range(0, index):
            opPush(opstack[-1 * index])
    except Exception as ex:
        print("Error in Copy()")
        debug(ex)
    return

def clear():
    while (len(opstack) > 0):
        opPop() # empty the stack

def stack():
    revo = reversed(opstack)
    print( " " )
    revAndIterd = reversed(list(enumerate(dictstack)))
    for item in revo:
        print(item)
    for (index, item) in revAndIterd:
        curTopStack, dictionary = item
        print("--", index, "--", curTopStack, "--")
        if dictionary:
            for key in dictionary:
                print(key, dictionary[key])
    print(" ")

# dictionary manipulation operators

def psDict():
    opPop()
    newDict = dict()
    opPush(newDict) 

def begin():
    if (len(opstack) > 0):
        op = opPop()
        if (type(op) == dict):
            dictPush(op) 
        else:
            opPush(op)
            print("Tried to push a non-dictionary on to the dict stack")
    else:
        print("Tried to pop a dictionary off of an empty op stack")


def end():
    if (len(dictstack) > 0):
        dictPop() 
    else:
        print("error: end()")

def psDef():
    value = opPop()
    name = opPop()
    if (type(name) == str):
        define(name, value)
    else:
        opPush(name)
        opPush(value)

#------------------------------- Parsing ---------------------------------------

import re
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c == '{':
            res.append(groupMatching2(it))
        else:
            res.append(c)
    return False

def parse(tokens):
    res = []
    it = iter(tokens)
    for c in it:
        if isinstance(c, list):
            res.append(parse(c))

        elif c == '}':
            return False

        elif c == '{':
            res.append(parse(groupMatching2(it)))

        elif c.isdigit():
            res.append(int(c))

        elif c.startswith('-'):
            res.append(int(c))

        elif c == "true" or c == "false":
            res.append(bool(c))

        elif c.startswith('['):
            newList = [int(num) for num in c[1:-1].split(' ')]
            res.append(newList)

        else:
            res.append(c)

    return res

def psIf():
    code = opPop()
    condition = opPop()

    if (condition == True):
        interpretSPS(code, scope)

def psIfElse():
    code2 = opPop()
    code1 = opPop()
    condition = opPop()

    if (condition == True):
        interpretSPS(code1, scope)

    else:
        interpretSPS(code2, scope)

def psFor():
    inputArray = opPop()
    stop = opPop()
    index = opPop()
    start = opPop()

    if index > 0:
	    for x in range(start, stop + 1, index):
		    opPush(x)
		    interpretSPS(inputArray, scope)

    elif index < 0:
	    for x in range(start, stop - 1, index):
		    opPush(x)
		    interpretSPS(inputArray, scope)

def psForAll():
    code = opPop()
    inputArray = opPop()

    for item in inputArray:
        opPush(item)
        interpretSPS(code, scope)
        
# interpreter 
functionDict = {"add": add, "sub": sub, "mul": mul, "div": div, "eq": eq, "gt": gt, "lt": lt, "length": length, "get": get, "and": psAnd, "or": psOr, "not": psNot, 
                "dup": dup, "exch": exch, "pop": pop, "copy": copy, "clear": clear, "stack": stack, "dict": psDict, "begin": begin, "end": end, "def": psDef, 
                "if": psIf, "ifelse": psIfElse, "for": psFor, "forall": psForAll}

def dictHelper(funcName):
    if funcName in functionDict.keys():
        return True
    else:
        return False

def interpretSPS(code, scope):
    for token in code:
        if isinstance(token, int) or isinstance(token, float) or isinstance(token, bool):
            opPush(token)

        elif isinstance(token, str):
            if token.startswith('/'):
                opPush(token)

            elif dictHelper(token):
                functionDict[token]()

            else:
                (index, lookFor) = lookup(token, scope)

                if (lookFor != None):
                    if isinstance(lookFor, list):
                        dictPush((index, {}))
                        interpretSPS(lookFor, scope)
                        dictPop()
                    
                    else:
                        opPush(lookFor)
        
        elif isinstance(token, list):
            opPush(token)

        else:
            print("Invalid code array type")

def interpreter(s, scope):
    print("Scope is currently: ", scope)
    interpretSPS(parse(tokenize(s)), scope)


# tests

def testinput1():
    input1 = """
        /x 4 def
        /g { x stack } def
        /f { /x 7 def g } def
        f
        """
    interpreter(input1, "static")
    opstack.clear()
    dictstack.clear()
    interpreter(input1, "dynamic")
    opstack.clear()
    dictstack.clear()

def testinput2():
    input2 = """
        /m 50 def
        /n 100 def
        /egg1 {/m 25 def n} def
        /chic {
            /n 1 def
            /egg2 { n } def
            m n
            egg1
            egg2
            stack } def
        n
        chic
        """
    interpreter(input2, "static")
    opstack.clear()
    dictstack.clear()
    interpreter(input2, "dynamic")
    opstack.clear()
    dictstack.clear()


def testinput3():
    input3 = """
        /x 10 def
        /A { x } def
        /C { /x 40 def A stack } def
        /B { /x 30 def /A { x } def C } def
        B
        """
    interpreter(input3, "static")
    opstack.clear()
    dictstack.clear()
    interpreter(input3, "dynamic")
    opstack.clear()
    dictstack.clear()


def testinput4():
    input4 = """
        /x 43 def
        /Z { /y 57 def x y add stack} def
        Z
        """
    interpreter(input4, "static")
    opstack.clear()
    dictstack.clear()
    interpreter(input4, "dynamic")
    opstack.clear()
    dictstack.clear()

def testinput5():
    input5 = """
        /a 500 def
        /b 25 def
        /C {a b div} def
        C stack
        """
    interpreter(input5, "static")
    opstack.clear()
    dictstack.clear()
    interpreter(input5, "dynamic")
    opstack.clear()
    dictstack.clear()

#----------------------------------------------------------

def main():
    testinput1()
    testinput2()
    testinput3()
    testinput4()
    testinput5()


if __name__ == '__main__':
    main()
