# cook your dish here
T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    if X<Y:
        print("FIRST")
    elif X == Y:
        print("ANY")
    else:
        print("SECOND")
