
a = input("type a number:")
a = int(a)

def f():
    global a
    return a/2

"if a function doesn't have a return, statement it returns None"
result = f()

def h():
    print(result*4)

h()



