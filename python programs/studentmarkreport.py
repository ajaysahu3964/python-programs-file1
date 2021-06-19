#studentmarks report.py
#validation of student number
while(True):
    sno=int(input("ENTER STUDENT NUMBER(1-200):"))
    if((sno>=1)and(sno<=200)):
         break
    #accepting name
    sname=int(input("ENTER STUDENT NAME:"))
    #validation mark in c
    while(True):
        cm=int(input("ENTER MARKS IN C :"))
    if((ccm>=0)and(ccm<=100)):
            break
    #validation marks in cpp
    while(True):
         cppm=int(input("ENTER MARKS IN CPPM:"))
    if((cppm>=0)and(cppm<=100)):
            break
     #validation marks in python
        
         while(True):
        pym=int(input("ENTER MARKS IN PY:"))
     if((py>=0)and(py<=100)):
             break
    #calculate total and percentage of marks
         totmarks =cm+cppm+pym
        percentagemarks=(totmarks/300)*100
    #give grade
    if ((cm<40)or(cppm<40)or(pym<40)):
                    grade="FAIL"
    else:
                    
        if((totmarks>=250)and(totmarks<=300)):
            grade="DISTINATION"
        elif((totmarks>=200)and(totmarks<=249)):
             grade="FIRST"
        elif((totmarks>=150)and(totmarks<=199)):
                grade="SECOND"
         elif((totmarks>=120)and(totmarks<=149)):
                 grade="THIRD"
                    #display sudent marks report
                    print("\t student marks report")
                    print("="*50)
                    print("\t student number:{}".format(sno))
                    print("\t student name:{}".format(sname))
                    print("\t student marks in c:{}".format(cm))
                    print("\t student marks in cppm:{}".format(cppm))
                    print("\t student marks in py:{}".format(pym))
                    print("="*50)
                    print("\t student total marks :{}".format(totmarks))
                    print("\t student percentage of marks:{}".format(percentagemarks))
                    print("="*50)
                    print("\t student result :{}".format(grade))
                    print("="*50)        
                                   
                                  
                                
                                
                
                          
        
