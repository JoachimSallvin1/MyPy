
import sys
import inspect 
from datetime import datetime #Using datetime 
import os # Use file name only in log printouts



# Hello.py
# The decorator takes extends the behavior of another function
# without changing the functions actual code.
# It takes the function as input arg and
# kwargs is a dictionary
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
    value="1"
    while value != "0":
        print("0.\t Exit")
        print("1.\t Log")
        print("2.\t User in")
        print("3.\t Out")
        print("4.\t Try if")
        print("5.\t Str")
        print("6.\t Bool")
        print("7.\t List")
        print("8.\t Tuple")
        print("9.\t Dictionary")
        print("10.\t Variadic args")
        print("11.\t While")

        value=input("Select function: ")
        print(f"Selected {value}...")
        match(value):
            case "0":
                print("Exit")
            case "1":
                log_function()
            case "2":     
                userInput = input("Enter your name: ")
                print("Welcome ",userInput)
                print("Python version",sys.version)
            case "3":   
                print(__name__)
            case "4":    
                tryIfFunction()
            case "5":    
                strFunction()
            case "6":    
                boolFunction()            
            case "7":
                listFunction()
            case "8":
                tupleFunction()
            case "9": 
                dictionaryFunction()
            case "10":
                varArgsFunction("First")
                varArgsFunction("Second",10,11,12)
                varArgsFunction("Second",10,11,12,key1="Val1",key2="val2",key3=3)
            case "11":
                whileFunction()
            case _:
                print("Default case")
    
@log_decorator
def whileFunction():
    i=0
    while i < 10:
      print(i)
      i+=1
    
@log_decorator
def dictionaryFunction():
    myDict={
        "Name": "Jocke",
        "Surename": "Sällvin",
        "Year": 1971
    }
    print(myDict)
    print(f"{myDict["Name"]} was born in {myDict["Year"]}")
    surename=myDict.get("Surename")
    print(f"Cognome={surename}")
    myDict["Surename"]="Andersson"
    print(f"Cognome={myDict.get("Surename")}")
    
    
def varArgsFunction(positional,*args, **kwargs):
    print(f"Positional: {positional}")    
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

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
        
