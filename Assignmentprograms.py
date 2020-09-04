
#PRIME

for i in range (1,200+1):
    count=0
    for k in range(1,i+1):
        if (i%k ==0):
            count+=1
            
    if (count==2):
        print(i)



#CONDITION
n=int(input("enter the number="))
if (n==1000):
      print("safe to land")
elif n<=4500:
    print(" bringit to 1000ft ")
else:
    print("turn around")


