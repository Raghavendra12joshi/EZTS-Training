

class voters:
    count=0
    while True:
        print("Voters list")
        print("1. raghu\n2. sachin\n")
        n = int(input("Enter your choice: "))
        u = {1: 'raghu',
             2: 'sachin'}

        print("Selected voter:", u[n])

        print("Voting members")
        print("1. bjp\n2. cong\n")
        a = int(input("Enter your choice: "))
        s = {1: 'bjp',
             2: 'cong'}
       
        print("Selected party:", s[a])

        if n == 1:
            if a == 1:
                print("raghu voted for bjp")
            else:
                print("raghu voted for cong")
        elif n == 2:
            if a == 1:
                print("sachin voted for bjp")
            else:
                print("sachin voted for cong")
       
        print("Count of votes:")
        if s[a] == 'bjp':
            bjp_count=count+1
            print("The winner is bjp")
       
        elif s[a] == 'cong':
             cong_count=count+1
             print("The winner is cong")
        
        choice = input("Do you want to continue voting? (yes/no): ")
        if choice.lower() != 'yes':
            break
voters()