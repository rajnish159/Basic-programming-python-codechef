# cook your dish here
T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    if X==0:
        print("Liquid")
    elif Y ==0:
        print("Solid")
    else:
        print("Solution")
        
