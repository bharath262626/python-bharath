import sys

def add(n, m):
    a = n + m
    return a

def sub(n, m):
    s = n - m
    return s

def mult(n, m):
    mult = n * m 
    return mult

n = sys.argv[1]
operation = sys.argv[2]
m = sys.argv[3]

if operation == "add":
    output = add(n, m)
    print(output)

elif operation == "sub":
     output = sub(n, m)
     print(output)

else:
    print("Unknown operation. Use add or sub.")
    sys.exit(1)
print(output)


