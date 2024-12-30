
import sys
import inspect 
from datetime import datetime #Using datetime 
import os # Use file name only in log printouts



# Hello.py
def log_decorator(func):
    def wrapper(*args, **kwargs):
        # 
        frame = inspect.currentframe().f_back
        fullPath = frame.f_code.co_filename
        fileName = os.path.basename(fullPath)
        lineNumber = frame.f_lineno
        timeStamp = datetime.now().strftime("%Y%m%d %H:%M:%S")
        print(f"{fileName} L:{lineNumber} {timeStamp}")
        return func(*args,**kwargs)
    return wrapper
    
def log_function():
    #Use f_back to step back in the stack so find the function that called log_function()
    print(f"*** {inspect.currentframe().f_back.f_code.co_name} ***")
@log_decorator
def main():
    log_function()
    ##userInput = input("Enter your name: ")
    ##print("Welcome ",userInput)
    print("Python version",sys.version)
    #print(__name__)
    #tryIfFunction()
    #strFunction()
    boolFunction()
    listFunction()
    tupleFunction()

@log_decorator
def listFunction():
    log_function()
    myList=["CLOSED","OPENING","OPENED","CLOSING"]
    myList.append("LOCKING")
    for i in range(len(myList)):
        print(myList[i])
    print(myList)
    myList.insert(2,"LOCKED")
    for x in myList:
        print(x)

@log_decorator        
def tupleFunction():
    log_function()
    myTuple=("A","B","C")
    print(myTuple)
    for j in myTuple:
        print(j)
    print(myTuple[1])
    tuple2 = myTuple[2]
    print(tuple2)    


@log_decorator    
def strFunction():
    log_function()
    inputAge=input("Please enter your age: ")
    txt=f"My name is J and I am {inputAge} years old."
    print(txt)

@log_decorator
def boolFunction():
    log_function()
    print(10>9)

@log_decorator    
def tryIfFunction():
    log_function()
    try:
        inputNumber=float(input("Enter a number: "))
        print(type(inputNumber))
        if inputNumber > 2:
            print(inputNumber,"> 2")
        else:
            print(inputNumber,"<= 2")
    except ValueError:
        print("Please enter a valid number.")
    
if __name__ == "__main__":
        main()
        
