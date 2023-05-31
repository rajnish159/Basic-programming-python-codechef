# cook your dish here
T = int(input())
for i in range(T):
    X = int(input())
    if X%2==0 and X%7==0:
        print("Alice")
    elif X%2 !=0 and X%9 ==0:
        print("Bob")
    else:
        print("Charlie")