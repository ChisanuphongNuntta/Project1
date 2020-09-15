def main():
    try:
        a,b = map(int,input("Input 2 integer values : ").split())
        s = divide(a, b)
    except Exception as err:
        print(err)
    else:
        print("resuit is",s)
    finally:
        print("excuting finally clause")
    

def divide(x,y):
    result = x / y
    return(result)
main()