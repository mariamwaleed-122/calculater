# calculater
print("welcom to you")
math=input("please choice a math operation (addition/subtraction/multiplication/divison)")

if math== "addition":
    a=int(input("please write fnumber"))
    a2=int(input("please write snumber"))
    print(a+a2)

if math== "subtraction":
     a=int(input("please write fnumber"))
     a2=int(input("please write snumber"))
     print(a-a2)

if math== "multiplication":
     a=int(input("please write fnumber"))
     a2=int(input("please write snumber"))
     print(a*a2)     

if math== "divison":
     a=int(input("please write fnumber"))
     a2=int(input("please write snumber"))
     if a or a2 ==0:
        print("sorry somthing wrong try again after latter")
     else:   
       print(a/a2)          
else:
    print("the math operation is done")