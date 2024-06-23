import datetime
def sportdata():
    while True:
        l=[101,102,103,104,105]
        print("1.101\n2.102\n3.103\n4.104\n5.105\n")
        a=int(input("equipment id"))
        if l[a] in l:
            print("equipment found=")
            print(l[a])
        else:
            print("no equipments are in list")
        print("equipments avalible")
        print("1.bat\n2.ball\n3.basket ball\n4.foot ball\n5.volley ball\n6.tennnis\n7.racket\n8.cock\n")
        while True:
            n=int(input())
            s={1:'bat',
               2:'ball',
               3:'basket ball',
               4:'foot ball',
               5:'volley ball',
               6:'tennnis',
               7:'racket',
               8:'cock'
               }
            if n in s:
                print("equipment found")
                print(s[n])
            else:
                print("equipment not found")
            print("condition of equipment items")
            print("1.good\n2.average\n3.bad")
            t=('good','average','bad') 
            b=int(input("equipment condition is"))
            if t[b] in t:
                print("show condition of equipment")
                print(t[b])
            else:
                print("equipment not found")
            print("1.enter name\n2.enter usn\n3.branch\n4.eid\n5.time for borrowing\n6.time of return")
            n=input("enter name")
            u=input("enter usn")
            b=input("enter branch")
            eid=int(input("equipment id"))
            tob_current_datetime = datetime.datetime.now()
            print("Current date and time:",tob_current_datetime)
            print("name is=",n)
            print("usn is=",u)
            print("branch is=",b)
            print("eid is=",eid)
            tor_current_datetime = datetime.datetime.now()
            print("Current date and time:",tor_current_datetime) 
            
            l=int(input("enter same eid"))
            if l==eid:
                print("equipment returned")
            else:
                print("equipment is not returned so return it")
            return n,u,b,eid,tob_current_datetime  
sportdata() 


    
    
     
        
        
        
  
    

            