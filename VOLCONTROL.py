# cook your dish here
T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    X = abs(X-Y)
    print(X)
