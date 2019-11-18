# Taryn Burns

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

# ------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
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


# -------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  # assuming top of the stack is the end of the list


# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name

# pops value off of dict stack
def dictPop():
    if (len(dictstack) > 0):
        return dictstack.pop()
    else:
        print("No dictionaries in dict stack")
    # dictPop pops the top dictionary from the dictionary stack.

    # dict pushes dict d to dictstack
    # Note that, your interpreter will call dictPush only when Postscript
    # begin op is called, begin should pop empty dict from
    # the opstack and push it onto the dictstack by calling dictPush.
# pushes value onto dictstack
def dictPush(d):
    dictstack.append(d)

    # add name:value pair to the top dictionary in the dictionary stack.
    # Keep the '/' in the name constant.
    # Your psDef function should pop the name and value from operand stack and, call define
# defines name and a value to the dictstack
def define(name, value):
    dictionary = dict()
    dictionary[name] = value
    dictPush(dictionary)

    # return the value associated with name
# whats design decision about what to do when theres no defn for name if name isnt defind
# your program should not break, but should give an appropriate error message.
# looks up name in dictstack
def lookup(name):
    for d in reversed(dictstack):
        if d.get('/'+name):
            return d.get('/'+name)
    return None
    #aname = '/' + name
    #reversedstack = reversed(dictstack)
    # for dictionary in reversedstack:
    #    if aname in dictionary:
    #        return dictionary[aname]
    #print("Name isn't defined in lookup.")



# --------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.
# adds values together in the opstack
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
     opPush(op1 < op2)

# checks to see if one value op1 is greater than op2
def gt():
    op1 = opPop()
    op2 = opPop()
    opPush(op1 > op2)  # push true if op1 > op2


# --------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, put, aload, astore

# gets length of opstack
def length():
    if (len(opstack) > 0):
        op = opPop()
        if (type(op) == list):
            opPush(len(op))
        else:
            opPush(op)

#
def get():
    if (len(opstack) > 0):
        num = opPop()
        currentList = opPop()
        if (type(num) == int and type(currentList) == list):
            opPush(currentList[num])
        else:
            opPush(currentList)
            opPush(num)
            print("Error in get()")
    else:
        print("Opstack is empty. Get() cant function properly")

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



# --------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
#duplicates the opstack
def dup():
    if (len(opstack) > 0):
        op1 = opPop()
        opPush(op1)
        opPush(op1)
    else:
        debug("Error in dup()")
    # op = opPop()
    # opPush(op)
    # opPush(op)

# copies opstack
def copy():
    index = opPop()
    try:
        for i in range(0, index):
            opPush(opstack[-1 * index])
    except Exception as ex:
        print("Error in Copy()")
        debug(ex)
    return

    num = opPop()
    if (type(num) == int and num < len(opstack)):
        opstack.extend(opstack[len(opstack) - num:])
    else:
        print("The value popped was not an int or the value was bigger than the length of op stack")

#  counts the number of occurrences a value appears from the stack
def count():
    op = opPop()
    len(opstack)

# pops value (op1) from opstack
def pop():
    if (len(opstack) > 0):
        op1 = opPop()
    else:
        debug("Error in pop()")

# clears opstack
def clear():
    if (len(opstack) > 0):
        while (len(opstack) != 0):
            opPop()
    else:
        debug("Error in clear()")

# exchanges op1 and op2 in opstack
def exch():
    if (len(opstack) > 1):
        op2 = opPop()
        op1 = opPop()
        opPush(op2)
        opPush(op1)
    else:
        debug("error in exch()")

def stack():
    while(len(opstack) > 0):
        op = opPop()
        print(op)
    #opstack.reverse()
    #for item in opstack:
    #    print(item)
    #opstack.reverse()

# --------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    op1 = opPop()
    d = {}
    opPush(d)


def begin():
    d = {}
    if (len(opstack) > 0):
        op = opPop()
        dictPush(d)
    else:
        debug("Error: begin()")


def end():
    if (len(dictstack) > 0):
        dictPop()
    else:
        debug("Error: end()")


def psDef():
    if (len(opstack) > 1):
        value = opPop()
        name = opPop()
        if type(name) == str:  # name[0] == '/': #(isinstance[name, str]):
            define(name, value)
        else:
            debug("Error psDef() invalid name")
    else:

        debug("Error: psDef()")

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# Test Cases
def test_define():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def test_lookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

def test_add():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def test_subtract():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def test_multiply():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def test_eq():
    opPush(6)
    opPush(6)
    eq()
    if opPop() != True:
        return False
    else:
        return True

def test_lt():
    opPush(6)
    opPush(3)
    lt()
    if opPop() != True:
        return False
    return True

def test_gt():
    opPush(3)
    opPush(6)
    gt()
    if opPop() != True:
        return False
    return True

def test_length():
    opPush([1, 2, 3, 4, 5])
    length()
    if opPop() != 5:
        return False
    return True

def test_get():
    opPush([1, 2, 3, 4, 5])
    opPush(4)
    get()
    if opPop() != 5:
        return False
    return True

def test_put():
    opPush(1)
    opPush(4)
    opPush(5)
    opPush(6)
    opPush(7)
    put()
    return True

def test_aload():
    pass

def test_astore():
    pass

def test_dup():
    opPush(10)
    dup()
    if opPop() != opPop():
        return False
    return True

def test_copy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if (opPop() != 5 and opPop() != 4 and opPop() != 5 and opPop() != 4 and
                opPop() != 3 and opPop() != 2):
        return False
    return True

def test_count():
    opPush(2)
    opPush(3)
    opPush(2)
    opPush(4)
    opPush(2)
    len(opstack)
    return True

def test_pop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2 = len(opstack)
    if(l1 != l2):
        return False
    return True

def test_clear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack) != 0:
        return False
    return True


def test_exch():
    opPush(10)
    opPush("/x")
    exch()
    if (opPop() != 10 and opPop() != "/x"):
        return False
    return True


def test_psdict():
    opPush(1)
    psDict()
    if opPop() != {}:
        return False
    return True

def test_begin():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    if lookup("x") != 3:
        return False
    return True

def test_end():
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x") != 3:
        return False
    return True


def test_psdef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x") != 10:
        return False
    return True
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

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


#--------------------------- if, ifelse, for, and forall ---------------------------

def psIf():
    code = opPop()
    condition = opPop()

    if (condition == True):
        interpretSPS(code)

def psIfElse():
    code2 = opPop()
    code1 = opPop()
    condition = opPop()

    if (condition == True):
        interpretSPS(code1)

    else:
        interpretSPS(code2)

def psFor():
    inputArray = opPop()
    stop = opPop()
    index = opPop()
    start = opPop()

    if index > 0:
	    for x in range(start, stop + 1, index):
		    opPush(x)
		    interpretSPS(inputArray)

    elif index < 0:
	    for x in range(start, stop - 1, index):
		    opPush(x)
		    interpretSPS(inputArray)

def psForAll():
    code = opPop()
    inputArray = opPop()

    for item in inputArray:
        opPush(item)
        interpretSPS(code)
        

def psAnd():
    op1 = opPop()
    op2 = opPop()
    # both ops true, push true, else false
    if (op1 == True and op2 == True):
        opPush(True)
    else:
        opPush(False)

def psOr():
    op1 = opPop()
    op2 = opPop()
    # either ops true, push true, else false
    if (op1 == True and op2 == False):
        opPush(True)
    elif (op1 == False and op2 == True):
        opPush(True)
    else:
        opPush(False)

def psNot():
    op = opPop()
    # push inverse of op
    if (op == True):
        opPush(False)
    elif (op == False):
        opPush(True)
#---------------------------- Interperet SPS Code and Code Arrays -----------------------------

functionDict = {"add": add, "sub": sub, "mul": mul, "eq": eq, "gt": gt, "lt": lt, "length": length, "get": get, "and": psAnd, "or": psOr, "not": psNot, 
                "dup": dup, "exch": exch, "pop": pop, "copy": copy, "clear": clear, "stack": stack, "dict": psDict, "begin": begin, "end": end, "def": psDef, 
                "if": psIf, "ifelse": psIfElse, "for": psFor, "forall": psForAll}

def dictHelper(funcName):
    if funcName in functionDict.keys():
        return True
    else:
        return False

def interpretSPS(code):
    for token in code:
        if isinstance(token, int) or isinstance(token, float) or isinstance(token, bool):
            opPush(token)

        elif isinstance(token, str):
            if token.startswith('/'):
                opPush(token)

            elif dictHelper(token):
                functionDict[token]()

            else:
                val = lookup(token)
                if not isinstance(val, list):
                    opPush(val)
                else:
                    interpretSPS(val)
        
        elif isinstance(token, list):
            opPush(token)

        else:
            print("Invalid code array type")

def interpreter(s):
    interpretSPS(parse(tokenize(s)))


# tests

def test1():
    input1 = """ 
        [1 2 3 4 5] dup length /n exch def
        /fact {
            0 dict begin
                /n exch def
                n 2 lt
                { 1}
                {n 1 sub fact n mul }
                ifelse
            end 
        } def
        n fact stack    
    """
    print("Test #1")
    print("Should be: \n120\n[1, 2, 3, 4, 5]")
    print("Evaluated to: ")
    interpreter(input1)
    print("\n----------------------------------------------\n")

    opstack.clear()
    dictstack.clear()


def test2():
    input2 = """
        [9 9 8 4 10] {dup 5 lt {pop} if} forall
        stack
    """

    print("Test #2")
    print("Should be: \n10\n8\n9\n9")
    print("Evaluated to: ")
    interpreter(input2)
    print("\n----------------------------------------------\n")

    opstack.clear()
    dictstack.clear()


def test3():
    input3 = """
        [1 2 3 4 5] dup length exch {dup mul} forall
        add add add add
        exch 0 exch -1 1 {dup mul add} for
        eq stack
    """
    print("Test #3")
    print("Should be: \nTrue")
    print("Evaluated to: ")
    interpreter(input3)
    print("\n----------------------------------------------\n")

opstack.clear()
dictstack.clear()


def test4():
    input4 = """
        /x 4 def
        /myf {
            /x x 1 add def
            1 dict begin
            /x 10 def
            x
            end
        } def
        x myf mul stack
    """

    print("Test #4")
    print("Should be: \n40")
    print("Evaluated to: ")
    interpreter(input4)
    print("\n----------------------------------------------\n")

    opstack.clear()
    dictstack.clear()


def test5():
    input5 = """
        /y 3 def
        /f {
           /z y def 1 dict
            begin
            /z 4 def
            /y 5 def
            z y mul
            end
        } def
        f y mul 60 eq
        { 1} 
        { 0}
        ifelse stack
    """
    print("Test #5")
    print("Should be: \n1")
    print("Evaluated to: ") 
    interpreter(input5)
    print("\n----------------------------------------------\n")

    opstack.clear()
    dictstack.clear()

def main():
    test1()
    test2()
    test3()
    test4()
    test5()

if __name__ == '__main__':
    main()
