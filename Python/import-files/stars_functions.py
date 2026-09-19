def RHSTW90OL(x,y,z):#right hand side triangle with  90 on left(no.ofrow:int,reverse:true/false,whichtype:true/false/none)
    if y:
        for i in range(1,x+1):
            if z:
                for j in range(1,i+1):
                    print("*",end=" ")
            elif z is None:
                for j in range(1,i+1):
                    print(f"{chr(64+i)}",end=" ")
            else:
                for j in range(1,i+1):
                    print(j,end=" ")
            print()
    else:
        for i in range(x,0,-1):
            if z:
                for j in range(1,i+1):
                    print("*",end=" ")
            elif z is None:
                for j in range(1,i+1):
                    print(f"{chr(64+i)}",end=" ")
            else:
                for j in range(1,i+1):
                    print(j,end=" ")
            print()
RHSTW90OL(5,True,True)
RHSTW90OL(5,False,True)
RHSTW90OL(5,True,False)
RHSTW90OL(5,False,False)
RHSTW90OL(5,True,None)
RHSTW90OL(5,False,None)