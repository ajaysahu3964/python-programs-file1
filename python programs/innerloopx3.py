#innerloopx3.py
nom=int(input("ENTER HOW MANY MULTIPLICATION TABLES U WANT:"))
if(nom<=0):
    print("{} invalid input".format(nom))
else:
    lst=list()
    for i in range (1,nom+1):
        print("ENTER A NUMBER FOR WHICH U WANT MUL TABLE:")
        v=int(input())
        lst.append(v)
    else:
        print("-------------")
        print("list values:", lst)
        for n in lst:
            print("-----------")
            print ("\t mul table for :{}". format(n))
            print("--------------------")
            for i in range(1,11):
                print("\t {}*{}={}".format (n,i,n*i))
            else:
                print("--------------------------")
         
