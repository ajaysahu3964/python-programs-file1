#innerloopex.py
nom=int(input("Enter hoe many multiplication tables u want :"))
if(nom<=0):
    print("{} invalid input". format(nom))
else:
    for n in range(1,nom+1):
        print("------------------")
        print("\t mul table for :{}".format (n))
        print("-------------------")
        for i in range(1,11):
            print("\t {}*{}={}".format (n,i,n*i))
        else:
            print("----------------")
        else:
        print("ALL MUL TABLE OVER")
