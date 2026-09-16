n=int(input("n:"))
print("Pattern A")
for i in range(1,n+1):
    for j in range(1,i+1):
            print(j,end=" ")
    print()
print("\nPattern B")
for i in range(n,0,-1):
    for j in range(1,i+1):
            print(j,end=" ")
    print()
print("\nPattern C")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
            print(j,end=" ")
    print()
print("\nPattern D")
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
            print(j,end=" ")
    print()