def main():
    a,b = map(int,input("Input 2 integer values : ").split())
    divide(a,b)

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("resuit is",result)
    finally:
        print("excuting finally clause")

main()