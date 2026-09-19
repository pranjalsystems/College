#temp
# program 1

# a=int(input("form of expression: ax²+bx+c=0\na:"))
# b=int(input("b:"))
# c=int(input("c:"))
# d=b**2-4*a*c
# def solveroot(a,b,d):
#     root1,root2=(-b+(d)**0.5)/(2*a),(-b-(d)**0.5)/(2*a)
#     return (root1,root2)
# if d>0:
#     print(f"determinant:{d}")
#     root1,root2=solveroot(a,b,d)
#     print(f"Roots:{root1},{root2}")
# if d==0:
#     print(f"determinant:{d}")
#     root1,root2=solveroot(a,b,d)
#     print(f"Roots:{root1}")
# if d<0:
#     print(f"determinant:{d}\nhence no real roots")

# program 2
# n=int(input("n:"))
# primelist=[]
# def checkp(x):
#     c=0
#     for i in range(2,x):
#         if x%i==0:c+=1
#     if c>0:return False
#     else:return True

# for i in range(2,n+1):
#     if checkp(i):primelist.append(i)
# print()
# if n in primelist:print(f"{n} is prime")
# else:print(f"{n} is not prime")

# print(f"\nPrime number till {n}")
# for i in primelist:
#     print(i,end=" ")
# print()

# fnpnumberslist=[]
# c2=0
# i=1
# while c2<=n:
#     if checkp(i):
#         fnpnumberslist.append(i)
#         c2+=1
#     i+=1

# print(f"\nFirst {n} Prime numbers")
# for i in fnpnumberslist:
#     print(i,end=" ")


# program 3
# n=int(input("n:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#             print("*",end=" ")
#     print()

# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#             print("*",end=" ")
#     print()

