#pati.py
n=int(input("ENTER HOW MANY STAR LINES U WANT:"))
if(n<=0):
    print("{} invalid input".format (n))
else:
    for i in range(0,n): 
     for j in range(0,i+1):
         print("*", end=" ")
         print()
         
