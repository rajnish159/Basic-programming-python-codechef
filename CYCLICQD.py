# cook your dish here
T = int(input())
for i in range(T):
    A, B, C, D = map(int, input().split())
    if A+C == 180 and B+D ==180:
        print("YES")
    else:
        print("NO")
