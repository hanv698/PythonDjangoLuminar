num1=int(input("num1"))
num2=int(input("num2"))

try:
    res=num1/num2
    print("Result:",res)
except:
    num2 = int(input("num2"))
    try:
        res = num1 / num2
        print("Result:", res)
    except Exception as e:
        print(e.args)
finally:
    print("Program completed")