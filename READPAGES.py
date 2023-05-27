# cook your dish here
T = int(input())
for i in range(T):
    N, X, Y = map(int, input().split())
    if N<=X*Y:
        print("YES")
    else:
        print("NO")
